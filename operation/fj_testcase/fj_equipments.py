from support.moc.equipment.fj_equipment import FjEquipment
from support.moc.equipment.equipment import Equipments

host = "192.168.1.5"
topic = "thing/data/post"
company_id = 1

fj_001_id = 22
rules_1 = [
    ("key", "default", "fj_001"),
    ("production", "increase", 1),
    ("electric_quantity", "increase", 0.1),
    ("status", "default", 0)
]
fj_001 = FjEquipment(fj_001_id, company_id, host, topic, rules=rules_1)

fj_002_id = 23
rules_2 = [
    ("key", "default", "fj_002"),
    ("production", "increase", 2),
    ("electric_quantity", "increase", 0.2),
    ("status", "take_turns", ([0, 1, 4], 10))
]
fj_002 = FjEquipment(fj_002_id, company_id, host, topic, rules=rules_2)

fj_003_id = 24
rules_3 = [
    ("key", "default", "fj_003"),
    ("production", "default", 0),
    ("electric_quantity", "default", 0),
    ("status", "default", 1)
]
fj_003 = FjEquipment(fj_003_id, company_id, host, topic, rules=rules_3)

fj_004_id = 25
rules_4 = [
    ("key", "default", "fj_004"),
    ("production", "default", 0),
    ("electric_quantity", "default", 0),
    ("status", "default", 4)
]
fj_004 = FjEquipment(fj_004_id, company_id, host, topic, rules=rules_4)

all_fj = Equipments(fj_001, fj_002, fj_003, fj_004)

fj_test = FjEquipment(fj_001_id, company_id, host, "test/1/thing/data/post", rules=rules_1)
fj_test2 = FjEquipment(fj_001_id, company_id, host, "test/2/thing/data/post", rules=rules_1)
test = Equipments(fj_test, fj_test2)
if __name__ == '__main__':
    # all_fj.delete()
    # all_fj.continue_publish()
    fj_test.continue_publish()
    # test.continue_publish()
