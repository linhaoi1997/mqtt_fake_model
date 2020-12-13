from support.moc.equipment.ay_equipment import AyEquipment, AyEquipments
from flask import Flask, jsonify, request
from operation.ay_testcase.aoya_configs import rules, rules2

company_id = 5

ay_thing_id_1 = 3
ay_001 = AyEquipment("001", company_id, ay_thing_id_1)
ay_001.import_rules(rules)
ay_001.add_rule("deviceStatus", "take_turns", (["9", "10"], 5))
ay_001.add_rule("total", "take_turns", ([0, 20, 30, 40, 50], 1))

ay_thing_id_2 = 4
ay_002 = AyEquipment("002", company_id, ay_thing_id_2)
ay_002.import_rules(rules)

ay_thing_id_3 = 7
ay_003 = AyEquipment("003", company_id, ay_thing_id_3)
ay_003.import_rules(rules2)

ay_thing_id_4 = 8
ay_004 = AyEquipment("004", company_id, ay_thing_id_4)
ay_004.import_rules(rules2)

ay_thing_id_5 = 9
ay_005 = AyEquipment("005", company_id, ay_thing_id_5)
ay_005.import_rules(rules)

ay_thing_id_6 = 10
ay_006 = AyEquipment("006", company_id, ay_thing_id_6)
ay_006.import_rules(rules)

all_ay = AyEquipments(ay_001, ay_002, ay_003, ay_004, ay_005, ay_006)
app = Flask(__name__)


@app.route('/iext/back/monitoring/DeviceMonitoringController/showDeviceMonitoringListOneToMany', methods=['GET'])
def get_tasks():
    return jsonify(all_ay.moc())


if __name__ == '__main__':
    # all_ay.delete()
    app.run(debug=True, host="0.0.0.0")
