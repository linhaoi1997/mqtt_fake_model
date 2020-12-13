from support.moc.mock_database import PostgresConn

database = "eam-test"

cockpit_info = {
    "user": "postgres",
    "password": "postgres",
    "host": "192.168.1.5",
    "port": 5432
}


def _find_id(thing_id, tag):
    eam_test = PostgresConn(database, cockpit_info)
    result = eam_test.query("select company_id,id,type_id,organization_id from things")
    for message in result:
        if message[1] == thing_id:
            if tag == "type":
                return message[2]
            elif tag == "company":
                return message[0]
            elif tag == "organization":
                return message[3]


type_id_map = {}


def find_type_id(thing_id):
    if type_id_map.get(str(thing_id)):
        return type_id_map.get(str(thing_id))
    else:
        result = _find_id(thing_id, "type")
        type_id_map[str(thing_id)] = result
        return result


company_id_map = {}


def find_company_id(thing_id):
    if type_id_map.get(str(thing_id)):
        return company_id_map.get(str(thing_id))
    else:
        result = _find_id(thing_id, "company")
        company_id_map[str(thing_id)] = result
        return result


organization_id_map = {}


def find_organization_id(thing_id):
    if type_id_map.get(str(thing_id)):
        return organization_id_map.get(str(thing_id))
    else:
        result = _find_id(thing_id, "organization")
        organization_id_map[str(thing_id)] = result
        return result


if __name__ == '__main__':
    s = find_type_id(3)
    print(s)
    s = find_company_id(3)
    print(s)
