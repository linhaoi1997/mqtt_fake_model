from support.moc.equipment.yt_equipment import YtEquipment

host = "192.168.1.5"
topic = "yt/thing/data/post"
test_001 = YtEquipment(host, topic)

test_002 = YtEquipment(host, topic)
test_002.set_default("devNo", "key1")

if __name__ == '__main__':
    test_001.set_default("speed", 0)
    test_001.set_default("G120_1", 0)
    test_001.publish_two()

    test_002.set_default("speed", 0)
    test_002.set_default("G120_1", 0)
    test_002.publish_two()