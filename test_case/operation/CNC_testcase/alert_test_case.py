from test_case.operation import cnc_1, cnc_2
from support.moc.equipment.cnc_equipment import CncStatus, CncAlarm
import datetime


class TestAlarm:

    def test_alarm_statistic(self):
        cnc_1.delete()
        input()
        # 报警码A 持续时间1h
        cnc_1.add_alarm(CncAlarm.A)
        cnc_1.publish_hour(hours=1)
        input()
        # 报警码B持续时间1h1min
        cnc_1.pop_alarm(CncAlarm.A)
        cnc_1.publish_hour(minutes=30)
        input()
        cnc_1.add_alarm(CncAlarm.B)
        cnc_1.publish_hour(hours=1, minutes=1)
        input()
        # 报警码C持续状态2min
        cnc_1.pop_alarm(CncAlarm.B)
        cnc_1.publish_hour(minutes=30)
        cnc_1.add_alarm(CncAlarm.C)
        cnc_1.publish_hour(minutes=2)
        input()
        # 报警码A持续状态1h
        cnc_1.pop_alarm(CncAlarm.C)
        cnc_1.add_alarm(CncAlarm.A)
        cnc_1.publish_hour(hours=1)
        input()

    def test_long_alarm(self):
        # 多次切换报警状态
        num = 0
        alarm = CncAlarm.ALL_ALARM[num % 3]
        cnc_1.add_alarm(alarm)
        for i in range(20):
            print("切换状态")
            cnc_1.publish_hour(minutes=1)
            num += 1
            cnc_1.pop_alarm(alarm)
            alarm = CncAlarm.ALL_ALARM[num % 3]
            cnc_1.add_alarm(alarm)

    def test_long_alarm_2(self):
        # 多次切换设备状态
        cnc_1.delete()
        num = 0
        status = CncStatus.All_STATUS[num % 4]
        cnc_1.change_state(status)
        for i in range(20):
            print("切换状态")
            cnc_1.publish_hour(minutes=1)
            num += 1
            status = CncStatus.All_STATUS[num % 4]
            cnc_1.change_state(status)

    def test_alert(self):
        cnc_1.delete()
        input()
        # 报警码A 持续时间5min
        cnc_1.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_1.add_alarm(CncAlarm.A)
        cnc_1.publish_hour(minutes=5, is_trigger=False)
        input()
        # 报警码B持续时间10min
        cnc_1.pop_alarm(CncAlarm.A)
        cnc_1.publish_hour(minutes=10)
        input()
        # 报警码A持续10min
        cnc_1.add_alarm(CncAlarm.A)
        cnc_1.publish_hour(minutes=10)

    def test_always_alert(self):
        cnc_2.delete()
        input()
        # 报警码A 持续时间5min
        cnc_2.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(hours=1)
        input()
        cnc_2.publish_hour(hours=1)


if __name__ == '__main__':
    # cnc_1.delete()
    test = TestAlarm()
    test.test_always_alert()
    # test.test_alarm_statistic()
    # test.test_alert()
