from support.moc.equipment.equipment import Equipment
from support.moc._format import *


class QsEquipment(Equipment):

    def __init__(self, thing_id, company_id, host, topic, config=None, rules=None):
        super(QsEquipment, self).__init__(thing_id, company_id, host, topic, qs_format, config, rules)
        self.ts_name = "ts"
