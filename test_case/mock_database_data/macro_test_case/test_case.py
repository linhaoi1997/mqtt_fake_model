import test_case.mock_database_data.macro_test_case.mock_data as m
from test_case.mock_database_data.macro_test_case import test
return_data = m.return_data


def do_1():
    # 查看同比/环比展示是否正常
    i = [
        # 奥亚
        ("2020-09-01 00:00:00", 3, "day", return_data(10, 10)),
        ("2020-08-01 00:00:00", 3, "day", return_data(10, 30)),
        ("2020-07-01 00:00:00", 3, "day", return_data(10, 20)),
        ("2020-06-01 00:00:00", 3, "day", return_data(10, 80)),
        ("2019-09-01 00:00:00", 3, "day", return_data(10, 5)),
        ("2019-08-01 00:00:00", 3, "day", return_data(10, 10)),
        ("2019-07-01 00:00:00", 3, "day", return_data(10, 20)),
        # 金立
        ("2020-09-01 00:00:00", 5, "day", return_data(10, 10)),
        ("2020-08-01 00:00:00", 5, "day", return_data(10, 30)),
        ("2020-07-01 00:00:00", 5, "day", return_data(10, 20)),
        ("2020-06-01 00:00:00", 5, "day", return_data(10, 80)),
        ("2019-09-01 00:00:00", 5, "day", return_data(10, 5)),
        ("2019-08-01 00:00:00", 5, "day", return_data(10, 10)),
        ("2019-07-01 00:00:00", 5, "day", return_data(10, 20)),
    ]
    test.insert_many(i)


def do_2():
    i = [
        # 奥亚
        ("2020-09-01 00:00:00", 3, "hour", return_data(10, 20)),
        ("2020-08-01 00:00:00", 3, "hour", return_data(10, 20)),
        ("2020-07-01 00:00:00", 3, "hour", return_data(10, 40)),
        ("2020-06-01 00:00:00", 3, "hour", return_data(10, 80)),
        ("2019-09-01 00:00:00", 3, "hour", return_data(10, 5)),
        ("2019-08-01 00:00:00", 3, "hour", return_data(10, 10)),
        ("2019-07-01 00:00:00", 3, "hour", return_data(10, 20)),
    ]
    test.insert_many(i)


def do_3():
    i = [
        # 奥亚
        ("2020-09-01 00:00:00", 3, "day", return_data(10, 20)),
        ("2020-08-01 00:00:00", 3, "day", return_data(10, 20)),

        ("2019-09-01 00:00:00", 3, "day", return_data(10, 5)),
        ("2019-08-01 00:00:00", 3, "day", return_data(10, 10)),
        # 王立
        ("2020-09-01 00:00:00", 5, "day", return_data(10, 30)),
        ("2020-09-06 00:00:00", 5, "day", return_data(10, 50)),
        ("2020-08-31 00:00:00", 5, "day", return_data(10, 20)),
        ("2020-08-30 00:00:00", 5, "day", return_data(10, 20)),
        ("2020-08-01 00:00:00", 5, "day", return_data(10, 20)),

        ("2019-09-01 00:00:00", 5, "day", return_data(10, 5)),
        ("2019-08-01 00:00:00", 5, "day", return_data(10, 10)),
    ]
    test.insert_many(i)


def do_4():
    # 企业经营分析
    i = [
        ("2020-09-01 00:00:00", 3, "day", return_data(20, 20)),
        ("2020-08-01 00:00:00", 3, "day", return_data(10, 20)),

        ("2019-09-01 00:00:00", 3, "day", return_data(10, 5)),
        ("2019-08-01 00:00:00", 3, "day", return_data(5, 10)),
        # 王立
        ("2020-09-01 00:00:00", 5, "day", return_data(20, 30)),
        ("2020-09-06 00:00:00", 5, "day", return_data(10, 50)),
        ("2020-08-31 00:00:00", 5, "day", return_data(10, 20)),
        ("2020-08-30 00:00:00", 5, "day", return_data(10, 20)),
        ("2020-08-01 00:00:00", 5, "day", return_data(10, 20)),

        ("2019-09-01 00:00:00", 5, "day", return_data(10, 5)),
        ("2019-08-01 00:00:00", 5, "day", return_data(10, 10)),
    ]
    test.insert_many(i)


def do_5():
    # 设备分析 月
    i = [
        # 奥亚
        ("2020-09-01 00:00:00", 3, "day", return_data(operation_time=2073600)),
        ("2020-08-01 00:00:00", 3, "day", return_data(operation_time=2142720)),

        ("2019-09-01 00:00:00", 3, "day", return_data(operation_time=2073600)),
        ("2019-08-01 00:00:00", 3, "day", return_data(operation_time=2142720)),

        ("2020-09-30 00:00:00", 4, "day", return_data(operation_time=2073600)),
        ("2020-08-31 00:00:00", 4, "day", return_data(operation_time=2142720)),

        ("2019-09-30 00:00:00", 4, "day", return_data(operation_time=2073600)),
        ("2019-08-31 00:00:00", 4, "day", return_data(operation_time=2142720)),
        # # 王立
        ("2020-09-01 00:00:00", 5, "day", return_data(operation_time=230399)),
        ("2020-08-01 00:00:00", 5, "day", return_data(operation_time=239039)),

        ("2019-09-01 00:00:00", 5, "day", return_data(operation_time=230399)),
        ("2019-08-01 00:00:00", 5, "day", return_data(operation_time=239039)),

        ("2020-09-30 00:00:00", 6, "day", return_data(operation_time=230399)),
        ("2020-08-31 00:00:00", 6, "day", return_data(operation_time=239039)),

        ("2019-09-30 00:00:00", 6, "day", return_data(operation_time=230399)),
        ("2019-08-31 00:00:00", 6, "day", return_data(operation_time=239039)),
    ]
    test.insert_many(i)


def do_6():
    # 设备分析-周
    o_t_1 = 7 * 3600 * 24 * 0.8
    o_t_2 = 7 * 3600 * 24 * 0.1 - 28801
    i = [
        # 奥亚
        # 上周下周
        ("2020-08-31 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        ("2020-08-24 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        # 去年此时
        ("2019-08-31 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        ("2019-08-24 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        # 第二台设备上周下周
        ("2020-08-31 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        ("2020-08-24 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        # 第二台设备去年此时
        ("2019-08-31 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        ("2019-08-24 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        # # 王立'
        # 上周下周
        ("2020-08-31 00:00:00", 5, "day", return_data(operation_time=o_t_2)),
        ("2020-08-24 00:00:00", 5, "day", return_data(operation_time=o_t_2)),
        # 去年此时
        ("2019-08-31 00:00:00", 5, "day", return_data(operation_time=o_t_2)),
        ("2019-08-24 00:00:00", 5, "day", return_data(operation_time=o_t_2)),
        # 第二台设备上周下周
        ("2020-08-31 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
        ("2020-08-24 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
        # 第二台设备去年此时
        ("2019-08-31 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
        ("2019-08-24 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
    ]
    test.insert_many(i)


def do_7():
    # 设备分析-天
    o_t_1 = 3600 * 24 * 0.8
    o_t_2 = 3600 * 24 * 0.1 - 28801
    i = [
        # 奥亚
        # 上天下天
        ("2020-08-31 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        ("2020-09-01 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        # 去年此时
        ("2019-08-31 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        ("2019-09-01 00:00:00", 3, "day", return_data(operation_time=o_t_1)),
        # 第二台设备上天下天
        ("2020-08-31 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        ("2020-09-01 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        # 第二台设备去年此时
        ("2019-08-31 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        ("2019-09-01 00:00:00", 4, "day", return_data(operation_time=o_t_1)),
        # # 王立'
        # 上天下天
        ("2020-08-31 00:00:00", 5, "day", return_data(operation_time=o_t_2 + 1)),
        ("2020-09-01 00:00:00", 5, "day", return_data(operation_time=o_t_2)),
        # 去年此时
        ("2019-08-31 00:00:00", 5, "day", return_data(operation_time=o_t_2 + 1)),
        ("2019-09-01 00:00:00", 5, "day", return_data(operation_time=o_t_2)),
        # 第二台设备上天下天
        ("2020-08-31 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
        ("2020-09-01 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
        # 第二台设备去年此时
        ("2019-08-31 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
        ("2019-09-01 00:00:00", 6, "day", return_data(operation_time=o_t_2)),
    ]
    test.insert_many(i)


def do_8():
    # 设备分析-天
    i = [
        # 奥亚
        # 上天下天
        ("2020-08-31 00:00:00", 3, "day", return_data()),
        ("2020-09-01 00:00:00", 3, "day", return_data()),
        ("2020-08-31 00:00:00", 4, "day", return_data()),
        ("2020-09-01 00:00:00", 4, "day", return_data()),
    ]
    test.insert_many(i)


if __name__ == '__main__':
    # # 查看同比/环比展示是否正常
    # do_1()
    # # # 查看同比/环比展示是否正常
    # do_2()
    # # 查看企业单耗展示是否正常
    # do_3()
    # # 企业经营分析
    # do_4()
    # 设备分析 月
    # do_5()
    # # 设备分析-周
    # do_6()
    # 设备分析-天
    do_7()
    # 总开机率
    # do_8()
