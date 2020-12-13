from support.moc.equipment.equipment import Equipment
from support.moc._format import *
import datetime


class FjEquipment(Equipment):

    def __init__(self, thing_id, company_id, host, topic, config=None, rules=None):
        super(FjEquipment, self).__init__(thing_id, company_id, host, topic, fj_format, config, rules)
        self.moc.add_rule("timestamp", "multiple", 1000)
        self.ts_name = "timestamp"

    @staticmethod
    def date_str(_time):
        return _time.strftime("%Y-%m-%d %H:%M:%S")

    def pub_one_hour_ago(self):
        start = datetime.datetime.now() - datetime.timedelta(hours=1)
        end = datetime.datetime.now()
        self.public_time_slot(self.date_str(start), self.date_str(end))
