import psycopg2

cockpit_info = {
    "user": "postgres",
    "password": "postgres",
    "host": "192.168.1.5",
    "port": 5435,
    "database": "cockpit-test",
}


class PostgresConn(object):

    def __init__(self, _cockpit_info=None):
        if _cockpit_info is None:
            _cockpit_info = cockpit_info
        self.database = _cockpit_info.get("database")
        self.conn = psycopg2.connect(
            **_cockpit_info
        )
        self.cursor = self.conn.cursor()

    def query(self, query):
        # query_str = "SELECT * FROM user_role WHERE role_id =2;"
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchall()

    def update(self, update):
        self.cursor.execute(update)
        self.conn.commit()

    def __del__(self):
        self.conn.commit()
        self.conn.close()
        print(self.database + ' close')


class MockDatabase(object):

    def __init__(self, database="cockpit-test", _cockpit_info=None):
        if _cockpit_info is None:
            _cockpit_info = cockpit_info
            if database:
                _cockpit_info["database"] = database
        self.conn = PostgresConn(_cockpit_info)
        self._query = None
        self.args_num = 0

    @property
    def query(self):
        return self._query

    @query.setter
    def query(self, value: str):
        test = []
        num = 0
        for _str in value:
            if _str == "{":
                test.append(1)
            elif _str == "}":
                if test:
                    test.pop()
                    num += 1
                else:
                    raise Exception("解析错误")
        if test:
            raise Exception("解析错误")
        self._query = value
        self.args_num = num

    def insert(self, *args):
        args = self._format(*args)
        if len(args) != self.args_num:
            raise Exception("参数数量不对，应该为%s，但是传了%s" % (self.args_num, len(args)))
        query = self._query.format(*args)
        self.conn.update(query)

    def insert_many(self, many: list):
        for _i in many:
            self.insert(*_i)

    @staticmethod
    def _format(*args):
        return args


if __name__ == "__main__":
    test_moc = MockDatabase()
    test_moc.query = """
    INSERT INTO public.thing_report 
    ("timestamp", thing_id, company_id, tag, data, type_id) VALUES 
    ('{time_str}', {thing_id}, {company_id}, '{tag}', 
    '{data}', '{type_id}');
    """
    assert test_moc.args_num == 6
