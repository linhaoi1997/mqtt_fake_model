from test_case.mock_database_data.cockpit_test_case import test2 as test, return_data2 as return_data


# _delete.delete_thing_report()


def test_time_utilization():
    # 9月百分之五十，10月百分之七十五
    thing_id_1 = 12
    thing_id_2 = 13
    i = [
        ("2020-10-01 00:00:00", thing_id_1, return_data(thing_id_1, operation_time=28800, standby_time=28800)),
        ("2020-10-01 00:00:00", thing_id_2, return_data(thing_id_2, operation_time=28800, standby_time=28800)),
        ("2020-10-02 00:00:00", thing_id_1, return_data(thing_id_2, operation_time=43200, standby_time=14400)),
        ("2020-10-02 00:00:00", thing_id_2, return_data(thing_id_2, operation_time=43200, standby_time=14400)),
    ]
    test.insert_many(i)


def test_operation_rate():
    # 9月百分之五十，10月百分之七十五
    thing_id_1 = 16
    i = [
        ("2020-09-01 00:00:00", thing_id_1, return_data(thing_id_1, operation_time=28800, standby_time=28800)),
        ("2020-09-30 00:00:00", thing_id_1, return_data(thing_id_1, operation_time=28800, standby_time=28800)),
        ("2020-08-01 00:00:00", thing_id_1, return_data(thing_id_1, operation_time=43200, standby_time=14400)),
        ("2020-08-31 00:00:00", thing_id_1, return_data(thing_id_1, operation_time=43200, standby_time=14400)),
    ]
    test.insert_many(i)


if __name__ == '__main__':
    # test_time_utilization()
    test_operation_rate()
