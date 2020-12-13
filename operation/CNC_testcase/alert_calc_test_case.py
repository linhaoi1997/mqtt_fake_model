from operation.CNC_testcase.cnc_equipments import cnc_2
from support.moc.equipment.cnc_equipment import CncStatus, CncAlarm
import datetime


class TestAlarmCalc:
    def test_1(self):
        cnc_2.delete()
        input()
        # 报警码A 持续时间5min
        cnc_2.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=10)
        input()
        cnc_2.change_alarm(CncAlarm.B)
        cnc_2.publish_hour(minutes=10)

    def test_2(self):
        cnc_2.delete()
        input()
        cnc_2.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=10)
        input()
        cnc_2.publish_hour(minutes=10)

    def test_3(self):
        cnc_2.delete()
        input()
        cnc_2.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=5, is_trigger=False)
        cnc_2.pop_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=10)
        input()
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=10)

    def test_4(self):
        cnc_2.delete()
        input()
        cnc_2.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=5, is_trigger=False)
        cnc_2.pop_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=10)
        input()
        cnc_2.add_alarm(CncAlarm.B)
        cnc_2.publish_hour(minutes=10)

    def test_5(self):
        cnc_2.delete()
        input()
        cnc_2.now = datetime.datetime(2020, 9, 1, 9, 50)
        cnc_2.publish_hour(minutes=10)
        input()
        cnc_2.add_alarm(CncAlarm.A)
        cnc_2.publish_hour(minutes=10)


if __name__ == '__main__':
    test = TestAlarmCalc()
    test.test_5()

