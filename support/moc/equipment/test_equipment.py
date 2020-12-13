from support.moc.equipment.equipment import Equipment
from support.moc._format import *


class TestEquipment(Equipment):

    def __init__(self, host, topic, config=None, rules=None):
        super(TestEquipment, self).__init__(None, None, host, topic, test_format, config, rules)
        self.ts_name = "ts"

    def continue_publish(self):
        self.mqtt_fake.continue_publish(time_step=60)
