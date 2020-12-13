from support.moc._format import ay_format
from support.moc.data_format import Moc
from support.moc.delete import delete


class AyEquipment(object):

    def __init__(self, device_number, company_id, thing_id):
        self.thing_id = thing_id
        self.company_id = company_id
        self.moc = Moc(ay_format)
        self.moc.set_default("deviceNumber", device_number)
        self.moc.add_rule("timestamp", "multiple", 1000)
        self.ts_name = None

    def __getattr__(self, item):
        return getattr(self.moc, item)

    def delete(self):
        delete(self.thing_id, self.company_id)


class AyEquipments(object):

    def __init__(self, *args):
        self.equipments = args

    def moc(self):
        body_list = [equipment.generate() for equipment in self.equipments]
        return {
            'body': {
                'list': body_list
            },
            'msg': '操作成功！',
            'success': 1,
        }

    def delete(self):
        for equipment in self.equipments:
            equipment.delete()
