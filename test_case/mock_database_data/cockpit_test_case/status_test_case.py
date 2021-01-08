from test_case.mock_database_data.cockpit_test_case import test, return_data, _delete

_delete.delete_thing_real_data()


def test_alarm():
    # 报警一小时设备1个，报警设备两个
    thing_id_1 = 12
    thing_id_2 = 13
    i = [
        ("2020-10-01 00:00:00", thing_id_1, return_data(thing_id_1, "alarm", 3600001)),
        ("2020-10-01 00:00:00", thing_id_2, return_data(thing_id_2, "alarm", 3600000))
    ]
    test.insert_many(i)


def test_standby():
    # 待机一小时设备1个，待机设备两个
    thing_id_1 = 12
    thing_id_2 = 13
    i = [
        ("2020-10-01 00:00:00", thing_id_1, return_data(thing_id_1, "standby", 3600001)),
        ("2020-10-01 00:00:00", thing_id_2, return_data(thing_id_2, "standby", 3600000))
    ]
    test.insert_many(i)


def test_status():
    # 工作/关机状态各一个可以顺便测试下设备总数那一块
    thing_id_1 = 12
    thing_id_2 = 13
    i = [
        ("2020-10-01 00:00:00", thing_id_1, return_data(thing_id_1, "operation", 3600001)),
        ("2020-10-01 00:00:00", thing_id_2, return_data(thing_id_2, "shutdown", 3600000))
    ]
    test.insert_many(i)


if __name__ == '__main__':
    test_status()
