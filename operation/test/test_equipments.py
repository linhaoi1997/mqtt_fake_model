from support.moc.equipment.test_equipment import TestEquipment

host = "emqx.teletraan.io"
topic = "test/1/thing/data/post"
test_001 = TestEquipment(host, topic)

if __name__ == '__main__':
    test_001.set_default("speed", "10")
    test_001.publish()
