from support.moc.mock_database import MockDatabase
from support.moc.delete import CockpitDelete
import json
from mock_database_data.find_id import find_company_id, find_type_id

database = "cockpit-test"

test = MockDatabase(database)
query_str = """
    INSERT INTO public.thing_report 
    ("timestamp", thing_id, company_id, tag, data, type_id) VALUES 
    ('{}', {}, {}, '{}', '{}', '{}');
    """
test.query = query_str
_delete = CockpitDelete()
_delete.delete_thing_report()


def _format(*args):
    company_id = find_company_id(args[1])
    type_id = find_type_id(args[1])
    data = json.dumps(args[3])
    return args[0], args[1], company_id, args[2], data, type_id


test._format = _format


def return_data(production=10, electric_quantity=10, operation_time=28800):
    return {
        "production": production, "standby_time": 28800, "shutdown_time": 28800, "operation_time": operation_time,
        "energy_group_id": 3,
        "organization_id": 1, "time_utilization": 0.8333, "speed_utilization": 0,
        "electric_quantity": electric_quantity,
        "peak_electric_quantity": electric_quantity * 0.1,
        "sharp_electric_quantity": electric_quantity * 0.1,
        "normal_electric_quantity": electric_quantity * 0.2,
        "valley_electric_quantity": electric_quantity * 0.4
    }

    # peak:尖  sharp：峰  valley：谷  normal：平


def do_1():
    # 查看一个月是否正常统计
    i = [
        # 奥亚
        ("2020-08-01 00:00:00", 3, "day", _data),
        ("2020-08-31 00:00:00", 3, "day", _data),
        # ("2020-09-30 00:00:00", 3, "day", _data),
        ("2020-09-01 00:00:00", 3, "day", _data),
        # 王力
        ("2020-08-01 00:00:00", 5, "day", _data),
        ("2020-08-31 00:00:00", 5, "day", _data),
        # ("2020-09-30 00:00:00", 5, "day", _data),
        ("2020-09-01 00:00:00", 5, "day", _data),
        ("2020-09-06 00:00:00", 5, "day", _data),
        ("2020-09-07 00:00:00", 5, "day", _data),
    ]
    test.insert_many(i)


def do_2():
    # # 用电最高负荷
    i = [
        # 奥亚
        ("2020-08-30 00:00:00", 3, "hour", return_data(10, 220)),
        ("2020-08-31 00:00:00", 3, "hour", return_data(10, 221)),
        ("2020-09-01 00:00:00", 3, "hour", return_data(10, 222)),
        ("2020-09-06 00:00:00", 3, "hour", return_data(10, 223)),
        ("2020-09-07 00:00:00", 3, "hour", return_data(10, 224)),
    ]
    test.insert_many(i)


def do_3():
    # # 查看多个月展示是否正常
    i = [
        # 奥亚
        ("2020-09-01 00:00:00", 3, "day", return_data(10, 220)),
        ("2020-08-01 00:00:00", 3, "day", return_data(10, 220)),
        ("2020-07-01 00:00:00", 3, "day", return_data(10, 220)),
        ("2020-06-01 00:00:00", 3, "day", return_data(10, 221)),
        ("2020-05-01 00:00:00", 3, "day", return_data(10, 222)),
        ("2020-04-01 00:00:00", 3, "day", return_data(10, 223)),
        ("2020-03-01 00:00:00", 3, "day", return_data(10, 224)),
    ]
    test.insert_many(i)


def do_4():
    # # 查看多个周展示是否正常
    i = [
        # 奥亚
        ("2020-08-24 00:00:00", 3, "day", return_data(10, 220)),
        ("2020-08-17 00:00:00", 3, "day", return_data(10, 221)),
        ("2020-08-10 00:00:00", 3, "day", return_data(10, 222)),
        ("2020-08-03 00:00:00", 3, "day", return_data(10, 223)),
        ("2020-07-27 00:00:00", 3, "day", return_data(10, 224)),
        ("2020-07-20 00:00:00", 3, "day", return_data(10, 225)),
        ("2020-07-13 00:00:00", 3, "day", return_data(10, 226)),
    ]
    test.insert_many(i)


def do_5():
    # 查看多个日是否显示正常
    i = [
        # 奥亚
        ("2020-08-24 00:00:00", 3, "day", return_data(10, 220)),
        ("2020-08-23 00:00:00", 3, "day", return_data(10, 221)),
        ("2020-08-22 00:00:00", 3, "day", return_data(10, 222)),
        ("2020-08-21 00:00:00", 3, "day", return_data(10, 223)),
        ("2020-08-20 00:00:00", 3, "day", return_data(10, 224)),
        ("2020-08-19 00:00:00", 3, "day", return_data(10, 225)),
        ("2020-08-18 00:00:00", 3, "day", return_data(10, 226)),
        # ("2020-09-01 00:00:00", 3, "day", return_data(10, 226)),
    ]
    test.insert_many(i)


if __name__ == '__main__':
    _data = return_data()
    # 查看一个月是否正常统计
    do_1()
    # # 用电最高负荷
    # do_2()
    # # 查看多个月展示是否正常
    # do_3()
    # # 查看多个周展示是否正常
    # do_4()
    # 查看多个日是否显示正常
    # do_5()
