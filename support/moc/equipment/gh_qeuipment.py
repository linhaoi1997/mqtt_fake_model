from support.moc.equipment.equipment import Equipment
from support.moc._format import *
import datetime


class GhEquipment(Equipment):

    def __init__(self, thing_id, company_id, host, topic, config=None, rules=None):
        super(GhEquipment, self).__init__(thing_id, company_id, host, topic, gh_format, config, rules)
        self.ts_name = "time"

    @staticmethod
    def date_str(_time):
        return _time.strftime("%Y-%m-%d %H:%M:%S")

    def pub_one_hour_ago(self):
        start = datetime.datetime.now() - datetime.timedelta(hours=1)
        end = datetime.datetime.now()
        self.public_time_slot(self.date_str(start), self.date_str(end))

