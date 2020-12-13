import redis
import psycopg2

redis_info = {"host": "192.168.1.5", "port": 6379, "db": 2}
cockpit_info = {
    "database": "cockpit-test",
    "user": "postgres",
    "password": "postgres",
    "host": "192.168.1.5",
    "port": 5435
}
warehouse_info = {
    "database": "warehouse-test",
    "user": "postgres",
    "password": "postgres",
    "host": "192.168.1.5",
    "port": 5433
}


class BaseDelete(object):

    def __init__(self, thing_id, company_id, _info):
        self.info = _info
        self.thing_id = thing_id
        self.company_id = company_id


class RedisDelete(BaseDelete):

    def __init__(self, thing_id, company_id, _info=None):
        super().__init__(thing_id, company_id, _info)
        if _info is None:
            self.info = redis_info
        self.conn = redis.StrictRedis(**self.info)
        self._latest_key = "cockpit:latest:{}:{}".format(self.company_id, self.thing_id)
        self._statistic_key = "cockpit:statistic:{}:{}*".format(self.company_id, self.thing_id)

    def delete(self):
        self.conn.delete(self._latest_key)
        key_list = self.conn.keys(self._statistic_key)
        for key in key_list:
            self.conn.delete(key)
        print("redis 删除完毕")
        self.conn.close()
        print("redis 断开连接")


class PostgresDelete(BaseDelete):
    def __init__(self, thing_id=None, company_id=None, _info=None):
        super().__init__(thing_id, company_id, _info)
        if _info is None:
            self.info = cockpit_info

        self.conn = psycopg2.connect(**self.info)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()
        print("数据库连接关闭")

    def execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()


class CockpitDelete(PostgresDelete):
    def delete(self):
        self.execute("delete  from thing_real_data where thing_id = %s" % self.thing_id)
        self.execute("delete  from thing_report where thing_id = %s" % self.thing_id)
        self.execute("delete  from alert where thing_id = %s" % self.thing_id)
        print("Cockpit thing_id为%s的记录删除完毕" % self.thing_id)

    def delete_thing_report(self):
        self.execute("delete  from thing_report where thing_id = %s" % self.thing_id)
        print("删除thing_report")

    def delete_thing_real_data(self):
        self.execute("delete  from thing_real_data where thing_id = %s" % self.thing_id)
        print("删除thing_real_data")

    def delete_single_hour_data(self, time_str):
        command = "delete from thing_report where timestamp = '%s' and tag='hour'" % time_str
        print(command)
        self.execute(command)

    def delete_single_day_data(self, time_str):
        command = "delete from thing_report where timestamp = '%s' and tag='day'" % time_str
        print(command)
        self.execute(command)

    def delete_input_data(self, time_str):
        command = "delete from thing_input_data_record where timestamp = '%s'" % time_str
        print(command)
        self.execute(command)


class WarehouseDelete(PostgresDelete):
    def delete(self):
        self.execute("delete  from thing_data_%s where thing_id = %s" % (self.company_id, self.thing_id))
        print("warehouse thing_id为%s的记录删除完毕" % self.thing_id)


class Delete(object):
    def __init__(self):
        self.delete_list = []

    def add(self, d: BaseDelete):
        self.delete_list.append(d)

    def delete(self):
        for d in self.delete_list:
            d.delete()


# 使用mqtt client mock的数据想要把所有数据都清掉那么必须要把redis，cockpit，warehouse都清掉
def delete(thing_id, company_id):
    redis_test = RedisDelete(thing_id, company_id)
    cockpit_test = CockpitDelete(thing_id, company_id)
    warehouse_test = WarehouseDelete(thing_id, company_id, warehouse_info)
    test = Delete()
    test.add(redis_test)
    test.add(cockpit_test)
    test.add(warehouse_test)
    test.delete()


if __name__ == '__main__':
    test_thing_id = 14
    test_company_id = 8
    delete(test_thing_id, test_company_id)
