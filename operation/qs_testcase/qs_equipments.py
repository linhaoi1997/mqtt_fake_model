from support.moc.equipment.qs_equipment import QsEquipment
from support.moc.equipment.equipment import Equipments

host = "192.168.1.5"
topic = "bm/qs/0%s/data/post"
company_id = 3

qs_001_id = 12
qs_002_id = 13

rules = [
    ("e", "increase", 2),
    ("ts", "multiple", 1000),
    ("ia", "default", 0),
    (["ib", "ic", "ua", "ub", "uc"], "random", ([1, 10], "uniform"))
]
rules_2 = [
    ("e", "increase", 1),
    ("ts", "multiple", 1000),
    ("ia", "take_turns", ([0, 1, 2], 2)),
    (["ib", "ic", "ua", "ub", "uc"], "random", ([1, 10], "uniform"))
]
qs_001 = QsEquipment(qs_001_id, company_id, host, topic % qs_001_id, rules=rules)
qs_002 = QsEquipment(qs_002_id, company_id, host, topic % qs_002_id, rules=rules_2)

all_qs = Equipments(qs_001, qs_002)

if __name__ == '__main__':
    # all_qs.delete()
    all_qs.continue_publish()
    # all_qs.public_time_slot("2020-10-01 00:00:00", "2020-10-01 01:00:00")
