from support.moc.equipment.equipment import Equipment
from support.moc._format import *
import datetime


class CncStatus:
    RUNNING = "Running"
    STANDBY = "Standby"
    ALARM = "Alarm"
    OFFLINE = "Offline"
    All_STATUS = (RUNNING, STANDBY, ALARM, OFFLINE)


class SingleCncAlarm:
    def __init__(self, alarm_type, alarm_num, alarm_info):
        self.alarm_type = alarm_type
        self.alarm_num = alarm_num
        self.alarm_info = alarm_info


class CncAlarm:
    A = SingleCncAlarm("不知道为什么", "NORMAL_ALARM_001", "就是一个平常的报警")
    B = SingleCncAlarm("不知道为什么2", "NORMAL_ALARM_002", "就是一个平常的报警2")
    C = SingleCncAlarm("很显然的报警", "FAMOUS_ALARM_001", "一看就知道的报警")
    ALL_ALARM = (A, B, C)


class CncEquipment(Equipment):

    def __init__(self, thing_id, company_id, host, topic, config, rules=None):
        super(CncEquipment, self).__init__(thing_id, company_id, host, topic, cnc_format, config, rules)
        self.ts_name = "t"
        self.now = None
        self._alarm = []

    @property
    def alarm_type(self):
        return ";".join([i.alarm_type for i in self._alarm])

    @property
    def alarm_num(self):
        return ";".join([i.alarm_num for i in self._alarm])

    @property
    def alarm_info(self):
        return ";".join([i.alarm_info for i in self._alarm])

    def change_state(self, state):
        assert state in CncStatus.All_STATUS
        self.moc.set_default("CNC001.cncstate", state)

    def _set_alarm(self):
        self.moc.set_default("CNC001.alarmtype", self.alarm_type)
        self.moc.set_default("CNC001.alarmnum", self.alarm_num)
        self.moc.set_default("CNC001.alarminfo", self.alarm_info)

    def add_alarm(self, alarm: SingleCncAlarm):
        assert alarm in CncAlarm.ALL_ALARM
        self._alarm.append(alarm)
        self._set_alarm()
        self.change_state(CncStatus.ALARM)

    def pop_alarm(self, alarm: SingleCncAlarm):
        assert alarm in CncAlarm.ALL_ALARM
        self._alarm.pop(self._alarm.index(alarm))
        self._set_alarm()
        if not self._alarm:
            self.change_state(CncStatus.RUNNING)

    def change_alarm(self, alarm: SingleCncAlarm):
        self._alarm = []
        self.add_alarm(alarm)

    def date_str(self):
        return self.now.strftime("%Y-%m-%d %H:%M:%S")

    def publish_hour(self, start=None, hours=0, minutes=0, seconds=0, is_trigger=True):
        if start:
            self.now = start
        if not self.now:
            self.now = datetime.datetime.now() - datetime.timedelta(days=30)
        start = self.date_str()
        duration = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
        self.now = self.now + duration + datetime.timedelta(seconds=1)
        end = self.date_str()
        self.public_time_slot(start, end, time_step=10)
        if is_trigger:
            self.trigger_all_timing_mask(start, end)
