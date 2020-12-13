from support.moc.mock_database import MockDatabase
from support.moc.delete import CockpitDelete
import json
from mock_database_data.find_id import find_company_id, find_type_id, find_organization_id

database = "cockpit-test"
_delete = CockpitDelete()
test = MockDatabase(database)
test.query = """
    INSERT INTO public.thing_real_data 
    ("timestamp", thing_id, company_id, data, type_id) VALUES 
    ('{}', {}, {}, '{}', {});
    """


def _format(*args):
    company_id = find_company_id(args[1])
    type_id = find_type_id(args[1])
    data = json.dumps(args[2])
    return args[0], args[1], company_id, data, type_id


test._format = _format


def return_data(thing_id, status_type="alarm", duration=3600001):
    result = {
        "voltage_a": 0.1, "voltage_b": 0.1, "voltage_c": 0.1, "electricity_a": 0.6,
        "electricity_b": 0.6, "electricity_c": 0.6, "status_type": "alarm", "duration": 3600000,
        "organization_id": find_organization_id(thing_id)}
    return result


# 测试状态 插入到thing_report
test2 = MockDatabase(database)
test2.query = """
    INSERT INTO public.thing_report 
    ("timestamp", thing_id, company_id, tag, data, type_id) VALUES 
    ('{}', {}, {}, '{}', '{}', '{}');
    """


def _format2(*args):
    company_id = find_company_id(args[1])
    type_id = find_type_id(args[1])
    data = json.dumps(args[2])
    return args[0], args[1], company_id, "day", data, type_id


test2._format = _format2


def return_data2(thing_id, operation_time=28800, standby_time=28800, shutdown_time=28800):
    result = {
        "operation_time": operation_time,
        "standby_time": standby_time,
        "shutdown_time": shutdown_time,
        "organization_id": find_organization_id(thing_id)
    }
    return result
