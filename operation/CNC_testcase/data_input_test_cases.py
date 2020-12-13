from operation.CNC_testcase.cnc_equipments import cnc_5
import datetime


def test_1():
    cnc_5.delete()

    start = datetime.datetime.now() - datetime.timedelta(days=1)

    start_num = 0
    step = 1
    max_value = 1000
    rules = [
        ("CNC001.partname", "default", "test1"),
        ("CNC001.count", "increase", (start_num, step, max_value)),
    ]
    cnc_5.moc.import_rules(rules)
    cnc_5.publish_hour(start, hours=1)

    rules = [
        ("CNC001.partname", "default", "test2"),
        ("CNC001.count", "increase", (start_num, step, max_value)),
    ]
    cnc_5.moc.import_rules(rules)
    cnc_5.publish_hour(hours=1)

    rules = [
        ("CNC001.partname", "default", "test1"),
        ("CNC001.count", "increase", (start_num, step, max_value)),
    ]
    cnc_5.moc.import_rules(rules)
    cnc_5.publish_hour(hours=1)
    # 360个


if __name__ == '__main__':
    test_1()
