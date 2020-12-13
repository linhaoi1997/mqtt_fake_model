from support.moc.equipment.cnc_equipment import CncEquipment
from support.moc.equipment.equipment import Equipments

host = "192.168.1.5"
topic = "jw/cs/post/cnc-00%s"
company_id = 8

# 第一台设备
cnc_thing_id_1 = 14
cnc_1_config = {
    "CNC001.cncstate": "Standby",
    "CNC001.cncip": "192.168.1.5",
    "CNC001.toolnum": "1",
    "CNC001.spindleload": 10,
    "CNC001.spindlespeed": 10, "CNC001.spindlerate": 10, "CNC001.spindlespeedset": 10, "CNC001.feedspeed": 10,
    "CNC001.feedrate": 10, "CNC001.feedspeedset": "10",
    "CNC001.partname": "MDI.PRG",
    "CNC001.programname": "MDI.PRG",
    "CNC001.count": 200,
    "CNC001.targetcount": 1000,
    "CNC001.cuttingtime": 28800,
}

cnc_1 = CncEquipment(cnc_thing_id_1, company_id, host, topic % 1, cnc_1_config)

# 第二台设备
cnc_thing_id_2 = 15
cnc_2_config = {
    "CNC001.cncstate": "Standby",
    "CNC001.cncip": "192.168.1.6",
    "CNC001.toolnum": "2",
    "CNC001.spindleload": 20,
    "CNC001.spindlespeed": 20, "CNC001.spindlerate": 20, "CNC001.spindlespeedset": 20, "CNC001.feedspeed": 20,
    "CNC001.feedrate": 20, "CNC001.feedspeedset": "20",
    "CNC001.partname": "MDII.PRG",
    "CNC001.programname": "MDII.PRG",
    "CNC001.count": 300,
    "CNC001.targetcount": 1000,
    "CNC001.cuttingtime": 51200,
    "CNC001.alarmnum": "test_002"
}
rules = [
    ("CNC001.cncstate", "take_turns", (["Running", "Standby", "Offline"], 3)),
    ("CNC001.spindleload", "take_turns", ([10, 20, 30, 400], 3)),
    ("CNC001.spindlerate", "take_turns", ([10, 20, 30, 400], 3)),
    ("CNC001.spindlespeed", "take_turns", ([10, 20, 30, 400], 3)),
    ("CNC001.feedspeed", "take_turns", ([10, 20, 30, 400], 3)),
    ("CNC001.feedrate", "take_turns", ([10, 20, 30, 400], 3)),
    ("CNC001.aload", "random", ([0, 100], "randint")),
    ("CNC001.bload", "random", ([0, 100], "randint")),
    ("CNC001.cload", "random", ([0, 100], "randint")),
    ("CNC001.xload", "random", ([0, 100], "randint")),
    ("CNC001.yload", "random", ([0, 100], "randint")),
    ("CNC001.zload", "random", ([0, 100], "randint")),
    ("CNC001.partname", "take_turns", (["MDII.PRG", "MDI.PRG", "MDIII.PRG", "MDIV.PRG"], 30)),
    ("CNC001.count", "take_turns", ([0, 10, 20, 30], 30)),
]
cnc_2 = CncEquipment(cnc_thing_id_2, company_id, host, topic % 2, cnc_2_config, rules)

# 第三台设备
cnc_thing_id_3 = 16
cnc_3_config = {
    "CNC001.cncstate": "Alarm",
    "CNC001.cncip": "192.168.1.7",
    "CNC001.toolnum": "3",
    "CNC001.spindleload": 30,  # 主轴负载
    "CNC001.spindlespeed": 31,  # 主轴转速
    "CNC001.spindlerate": 32,  # 主轴倍率
    "CNC001.spindlespeedset": 33,  # 主轴设定转速
    "CNC001.feedspeed": 34,  # 进给轴转速
    "CNC001.feedrate": 35,  # 倍率
    "CNC001.feedspeedset": "36",  # 设定转速
    "CNC001.partname": "MDIII.PRG",
    "CNC001.programname": "MDII.PRG",
    "CNC001.count": 200,
    "CNC001.targetcount": 1000,
    "CNC001.cuttingtime": 28861,
    "CNC001.alarmnum": "test_003",
}
rules_2 = [
    ("CNC001.cncstate", "take_turns", (["Running", "Standby", "Alarm", "Running", "Standby", "Alarm"], 40)),
    ("CNC001.spindleload", "random", ([90, 100], "uniform")),
    ("CNC001.spindlespeed", "random", ([90, 100], "uniform")),
    ("CNC001.feedspeed", "random", ([90, 100], "uniform")),
    ("CNC001.spindlerate", "random", ([90, 100], "uniform")),
    ("CNC001.feedrate", "random", ([90, 100], "uniform")),
    ("CNC001.partname", "random", ([90, 100], "uniform")),
    ("CNC001.programname", "random", ([90, 100], "uniform")),
    ("CNC001.partname", "take_turns", (["test1", "test2", "test3", "test4"], 30)),
    ("CNC001.count", "take_turns", ([0, 100, 200, 300], 30)),
    ("CNC001.targetcount", "random", ([90, 100], "randint")),
    ("CNC001.cuttingtime", "increase", 10),
    ("CNC001.alarmnum", "take_turns", (["", "", "ERROR_1", "", "", "ERROR_2"], 40))
]
cnc_3 = CncEquipment(cnc_thing_id_3, company_id, host, topic % 3, cnc_3_config, rules_2)

# 第四台设备
cnc_thing_id_4 = 17
cnc_4_config = {
    "CNC001.cncstate": "Alarm",  # 测试时间稼动率分母为0的情况
    "CNC001.cncip": "192.168.1.8",
    "CNC001.toolnum": "4",
    "CNC001.spindleload": 40,
    "CNC001.spindlespeed": 40, "CNC001.spindlerate": 40, "CNC001.spindlespeedset": 40, "CNC001.feedspeed": 40,
    "CNC001.feedrate": 40, "CNC001.feedspeedset": "40",
    "CNC001.partname": "MDIIII.PRG",
    "CNC001.programname": "MDII.PRG",
    "CNC001.count": 200,
    "CNC001.targetcount": 1000,
    "CNC001.cuttingtime": 28800,
    "CNC001.alarmnum": "test_test"
}
cnc_4 = CncEquipment(cnc_thing_id_4, company_id, host, topic % 4, cnc_4_config)

# 第四台设备
cnc_thing_id_5 = 27
cnc_5_config = {
    "CNC001.cncstate": "Running",  # 测试时间稼动率分母为0的情况
    "CNC001.cncip": "192.168.1.9",
    "CNC001.toolnum": "4",
    "CNC001.spindleload": 40,
    "CNC001.spindlespeed": 40, "CNC001.spindlerate": 40, "CNC001.spindlespeedset": 40, "CNC001.feedspeed": 40,
    "CNC001.feedrate": 40, "CNC001.feedspeedset": "40",
    "CNC001.partname": "MDIIII.PRG",
    "CNC001.programname": "MDII.PRG",
    "CNC001.count": 200,
    "CNC001.targetcount": 1000,
    "CNC001.cuttingtime": 864060,
    "CNC001.alarmnum": "test_test"
}
cnc_5 = CncEquipment(cnc_thing_id_5, company_id, host, topic % 5, cnc_5_config)

all_cnc = Equipments(cnc_1, cnc_2, cnc_3, cnc_4)

if __name__ == '__main__':
    # all_cnc.delete()
    # all_cnc.continue_publish()
    cnc_5.delete()
    cnc_5.continue_publish()
    # cnc_5.wait_until_warehouse_complete()
