from test_case.operation import cnc_5, all_cnc
from support.moc.equipment.cnc_equipment import CncStatus


class TestStatus:

    def test_status(self):
        all_cnc.continue_publish()
        # 校验设备静态信息 和 动态信息模块

    def test_history_status(self):
        # cnc_2一直会切换状态，其他是单状态
        # all_cnc.delete()
        start_date = "2020-07-01 00:00:00"
        end_date = "2020-07-02 00:00:00"
        all_cnc.public_time_slot(start_date, end_date)

    def test_time_choice(self):
        # all_cnc.delete()
        start_date = "2020-08-01 00:00:00"
        end_date = "2020-08-02 00:00:00"
        all_cnc.public_time_slot(start_date, end_date)
        start_date = "2020-08-31 00:00:00"
        end_date = "2020-09-01 00:00:00"
        all_cnc.public_time_slot(start_date, end_date)
        start_date = "2020-09-30 00:00:00"
        end_date = "2020-10-02 00:00:00"
        all_cnc.public_time_slot(start_date, end_date)

    def test_time_utilization_1(self):
        # cnc_5.delete()
        # 开机1h
        cnc_5.change_state(CncStatus.RUNNING)
        start_date = "2020-10-03 00:00:00"
        end_date = "2020-10-03 01:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        cnc_5.change_state(CncStatus.OFFLINE)
        start_date = "2020-10-04 01:00:00"
        end_date = "2020-10-04 02:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        input()

    def test_time_utilization_2(self):
        # 开机1h待机2h
        cnc_5.change_state(CncStatus.RUNNING)
        start_date = "2020-10-05 00:00:00"
        end_date = "2020-10-05 01:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        cnc_5.change_state(CncStatus.STANDBY)
        start_date = "2020-10-05 01:00:00"
        end_date = "2020-10-05 03:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        input()

    def test_time_utilization_3(self):
        # 告警3h 这三条一起执行顺便看下历史状态-运行状态构成
        cnc_5.change_state(CncStatus.RUNNING)
        start_date = "2020-10-06 00:00:00"
        end_date = "2020-10-06 01:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        cnc_5.change_state(CncStatus.STANDBY)
        start_date = "2020-10-06 01:00:00"
        end_date = "2020-10-06 03:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        cnc_5.change_state(CncStatus.ALARM)
        start_date = "2020-10-06 03:00:00"
        end_date = "2020-10-06 06:00:00"
        cnc_5.public_time_slot(start_date, end_date)
        input()


if __name__ == '__main__':
    cnc_5.wait_until_warehouse_complete()
    # cnc_5.delete()
    test1 = TestStatus()
    # test1.test_time_choice()
    # test1.test_time_utilization_1()
    # test1.test_time_utilization_2()
    # test1.test_time_utilization_3()
