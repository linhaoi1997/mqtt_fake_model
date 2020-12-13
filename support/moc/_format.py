import time
import datetime

qs_format = {
    "ts": time.time,
    "params": {
        "e": 10,
        "ia": 0,
        "ib": 1,
        "ic": 1,
        "ua": 1,
        "ub": 1,
        "uc": 1
    }
}

cnc_format = {
    "data": [
        {"k": "CNC001.alarminfo", "v": ""}, {"k": "CNC001.alarmnum", "v": ""}, {"k": "CNC001.alarmtype", "v": ""},
        {"k": "CNC001.aload", "v": "10"}, {"k": "CNC001.bload", "v": "20"}, {"k": "CNC001.cload", "v": "30"},
        {"k": "CNC001.apos", "v": "1.08"},
        {"k": "CNC001.cncip", "v": "192.168.1.100"}, {"k": "CNC001.cncmode", "v": "MDI模式中"},
        {"k": "CNC001.cncstate", "v": "Standby"},
        {"k": "CNC001.cnctype", "v": "MITSUBISHI CNC 70VM-B  BND-1018W000-H5 "},
        {"k": "CNC001.count", "v": "71899"}, {"k": "CNC001.cuttingtime", "v": "36943493"},
        {"k": "CNC001.feedrate", "v": "150"}, {"k": "CNC001.feedspeed", "v": "0"},
        {"k": "CNC001.feedspeedset", "v": "0"}, {"k": "CNC001.partname", "v": "MDI.PRG"},
        {"k": "CNC001.powerontime", "v": "62986507"}, {"k": "CNC001.programname", "v": "MDI.PRG"},
        {"k": "CNC001.runningtime", "v": "37848495"}, {"k": "CNC001.spindleload", "v": "0"},
        {"k": "CNC001.spindlerate", "v": "100"}, {"k": "CNC001.spindlespeed", "v": "0"},
        {"k": "CNC001.spindlespeedset", "v": "0"}, {"k": "CNC001.targetcount", "v": ""},
        {"k": "CNC001.toolnum", "v": "0"}, {"k": "CNC001.xload", "v": "20"}, {"k": "CNC001.xpos", "v": "-382"},
        {"k": "CNC001.yload", "v": "30"}, {"k": "CNC001.ypos", "v": "0"}, {"k": "CNC001.zload", "v": "40"},
        {"k": "CNC001.zpos", "v": "0"}, {"k": "script_error", "v": None}, {"k": "CNC001.cycle_time", "v": 10},
    ],
    "meta": {"expire": 3600, "t": time.time}}

gh_format = {
    "gatew": "ec9c6f4a960c6e88",
    "time": time.time,  # - 48685538,
    "D34": 0,  # 产量计数 pcs
    "D462": 0 * 1000,  # 累计电量 kw.h

    "D438": 108187,  # 高频加热输入功率 kw  除1000
    "D528": 842,  # 功率因数   除1000

    "D22": 90,  # 每支钢管高频耗电 kw.h   除1000
    "D56": 194.68069458007813,  # 每支钢管高频耗电电流 A 除1000

    "D372": 15314,  # 每千米钢管高频耗电 kw.h 除1000
    "D368": 15331,  # 每千米钢管高频耗电 A 除1000

    "D31": 1111,  # 钢管线速度 M/min 除10
    "D30": 1400,  # 钢管最高线速度 M/min 除10

    "D32": 60100,  # 钢管长度设定值 mm  除10
}

fj_format = {
    "key": "0e6b4470-58f2-4e1f-a4c0-02e1eb5de446",
    "timestamp": time.time,
    "data": {
        "production": 0,
        "electric_quantity": 0,
        "status": 0
    }
}
ay_format = {
    "timestamp": time.time,
    'deviceNumber': '8501',
    'deviceType': '测试类型-2',
    "maintainType": "2",
    'deviceStatus': "9",  # 1待排产，2已排产，3待穿纱，4穿纱中，5待改机，6改机中，7待首检，8首检完成，9量产中，10量产完成，11下机关闭，12继续量产
    # 所有排产单，只有9，10
    'productSpecification': '1120D/320/150/150,黑色,普通',
    "total": 0,  # 当前产量
    'predictM': 10000,  # 目标产量
    'revolution': 0,  # 实际生产总时长
    'predictTime': 100000,  # 理论生产的总时长
    "workTime": 0,  # 今日生产总时长

    'dayWorkTimeTotal': 0,
    'deviceId': 8,
    'economicSpeed': 700,
    'orderNumber': 'AY12278',

    'productnum': 3,
    'schedule': 0.0,
    'serial': 2,
    'sort': 2,
    'workOrderId': 3335,
    'workOrderNumber': '20190802027',
}

test_format = {
    "ts": time.time,
    "test_str": 1
}


def return_now_time_str():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


yuantong_format = {
    "cmdId": 103, "devId": 1167, "devNo": "key2",
    "varList": {"G120_1": "0", "G120_2": "0", "G120_3": "0", "G120_4": "0",
                "G120_5": "0", "G120_6": "0", "G120_7": "136.30", "G120_8": "145.30",
                "G120_9": "-0.00", "G120_10": "-0.00", "G120_11": "-0.00", "G120_12": "-0.00",
                "G120_13": "-0.00", "G120_14": "-0.00", "G120_15": "170.30", "G120_16": "-0.00",
                "G120_17": "-0.00", "G120_18": "-0.00", "G120_19": "-0.00", "G120_20": "-0.00",
                "G120_21": "-0.00", "G120_22": "-0.00", "G120_23": "-0.00", "G120_24": "-0.00",
                "G120_25": "-0.00", "G120_26": "-0.00", "specifications_code": "19575.00",
                "speed": "0", "current": "127.15", "voltage": "10.27", "big_speed": "0.77"},
    "type": 0, "ver": "0.1.3.10", "time": return_now_time_str
}
