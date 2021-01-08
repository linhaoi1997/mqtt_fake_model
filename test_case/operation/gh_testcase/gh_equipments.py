from support.moc.equipment.gh_qeuipment import GhEquipment
from support.moc.equipment.equipment import Equipments

host = "192.168.1.5"
topic = "yx/thing/data/post"
company_id = 2

gh_001_id = 18
rules = [
    ("gatew", "default", "gh_001"),
    ("D34", "increase", 1),  # 产量计数 pcs
    ("D462", "increase", 1000),  # 累计电量 kw.h
    ("D438", "random", ([108187, 208187], "uniform")),  # 高频加热输入功率 kw  除1000
    ("D528", "random", ([842, 1842], "uniform")),  # 功率因数   除1000
    ("D22", "random", ([90, 190], "uniform")),  # 每支钢管高频耗电 kw.h   除1000
    ("D56", "random", ([194, 294], "uniform")),  # 每支钢管高频耗电电流 A 除1000
    ("D372", "random", ([15314, 25314], "uniform")),  # 每千米钢管高频耗电 kw.h 除1000
    ("D368", "random", ([15331, 25331], "uniform")),  # 每千米钢管高频耗电 A 除1000
    ("D31", "take_turns", ([0, 10, 20, 30], 5)),  # 钢管线速度 M/min 除10
    ("D30", "random", ([1400, 2400], "uniform")),  # 钢管最高线速度 M/min 除10
    ("D32", "take_turns", ([60100, 60200, 60300], 5))  # 钢管长度设定值 mm  除10)
]
gh_001 = GhEquipment(gh_001_id, company_id, host, topic, rules=rules)

gh_002_id = 19
rules_2 = [
    ("gatew", "default", "gh_002"),
    ("D34", "increase", 0),  # 产量计数 pcs
    ("D462", "increase", 1000),  # 累计电量 kw.h
    ("D438", "random", ([108187, 208187], "uniform")),  # 高频加热输入功率 kw  除1000
    ("D528", "random", ([842, 1842], "uniform")),  # 功率因数   除1000
    ("D22", "random", ([90, 190], "uniform")),  # 每支钢管高频耗电 kw.h   除1000
    ("D56", "random", ([194, 294], "uniform")),  # 每支钢管高频耗电电流 A 除1000
    ("D372", "random", ([15314, 25314], "uniform")),  # 每千米钢管高频耗电 kw.h 除1000
    ("D368", "random", ([15331, 25331], "uniform")),  # 每千米钢管高频耗电 A 除1000
    ("D31", "default", 0),  # 钢管线速度 M/min 除10
    ("D30", "random", ([1400, 2400], "uniform")),  # 钢管最高线速度 M/min 除10
    ("D32", "take_turns", ([60100, 60200, 60300], 5))  # 钢管长度设定值 mm  除10)
]
gh_002 = GhEquipment(gh_002_id, company_id, host, topic, rules=rules_2)

gh_003_id = 20
rules_3 = [
    ("gatew", "default", "gh_003"),
    ("D34", "increase", 2),  # 产量计数 pcs
    ("D462", "increase", 2000),  # 累计电量 kw.h
    ("D438", "random", ([108187, 208187], "uniform")),  # 高频加热输入功率 kw  除1000
    ("D528", "random", ([842, 1842], "uniform")),  # 功率因数   除1000
    ("D22", "random", ([90, 190], "uniform")),  # 每支钢管高频耗电 kw.h   除1000
    ("D56", "random", ([194, 294], "uniform")),  # 每支钢管高频耗电电流 A 除1000
    ("D372", "random", ([15314, 25314], "uniform")),  # 每千米钢管高频耗电 kw.h 除1000
    ("D368", "random", ([15331, 25331], "uniform")),  # 每千米钢管高频耗电 A 除1000
    ("D31", "take_turns", ([100, 200, 300], 5)),  # 钢管线速度 M/min 除10
    ("D30", "random", ([1400, 2400], "uniform")),  # 钢管最高线速度 M/min 除10
    ("D32", "take_turns", ([60100, 60200, 60300], 5))  # 钢管长度设定值 mm  除10)
]
gh_003 = GhEquipment(gh_003_id, company_id, host, topic, rules=rules_3)

gh_004_id = 21
rules_4 = [
    ("gatew", "default", "gh_004"),
    ("D34", "increase", 1),  # 产量计数 pcs
    ("D462", "increase", 1000),  # 累计电量 kw.h
    ("D438", "random", ([108187, 208187], "uniform")),  # 高频加热输入功率 kw  除1000
    ("D528", "random", ([842, 1842], "uniform")),  # 功率因数   除1000
    ("D22", "random", ([90, 190], "uniform")),  # 每支钢管高频耗电 kw.h   除1000
    ("D56", "random", ([194, 294], "uniform")),  # 每支钢管高频耗电电流 A 除1000
    ("D372", "random", ([15314, 25314], "uniform")),  # 每千米钢管高频耗电 kw.h 除1000
    ("D368", "random", ([15331, 25331], "uniform")),  # 每千米钢管高频耗电 A 除1000
    ("D31", "take_turns", ([0, 10, 20, 30], 5)),  # 钢管线速度 M/min 除10
    ("D30", "random", ([1400, 2400], "uniform")),  # 钢管最高线速度 M/min 除10
    ("D32", "take_turns", ([60100, 60200, 60300], 5))  # 钢管长度设定值 mm  除10)
]
gh_004 = GhEquipment(gh_004_id, company_id, host, topic, rules=rules_4)

all_gh = Equipments(gh_001, gh_002, gh_003, gh_004)

if __name__ == '__main__':
    all_gh.continue_publish()
