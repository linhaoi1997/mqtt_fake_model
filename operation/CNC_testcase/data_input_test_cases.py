from operation.CNC_testcase.cnc_equipments import cnc_5
import datetime
import pytest

cnc = cnc_5
_start_date = '2021-01-05 00:00:00'
_end_date = '2021-01-06 00:00:00'
start = datetime.datetime.strptime('2021-01-05', "%Y-%m-%d")


def publish(production_name, hours, start_date=None, is_trigger=False, start_num: float = 100):
    step = 1
    max_value = 10000

    rules = [
        ("CNC001.partname", "default", production_name),
        ("CNC001.count", "increase", (start_num, step, max_value)),
    ]
    cnc.moc.import_rules(rules)
    cnc.publish_hour(start_date, hours=hours, is_trigger=is_trigger)


def cal():
    cnc_5.trigger_all_timing_mask(_start_date, _end_date)


class TestDataInput:

    @pytest.fixture(scope="function", autouse=True)
    def init(self):
        print("zhixing")
        cnc.delete()

    def test_1(self, init):
        # 1h360个
        publish("test1", 2.5, start)
        publish("test2", 2)
        publish("test3", 2)
        publish("test1", 2, start_num=0)
        publish("test2", 2, is_trigger=True, start_num=0)

        # 调用定时任务计算
        cal()

        assert cnc_5.query_production(_start_date, "test1") == 1620
        assert cnc_5.query_production(_start_date, "test2") == 1440
        assert cnc_5.query_production(_start_date, "test3") == 720

    # def test_2(self):
    #     # 1h360个
    #     publish("test1", 2.5, start)
    #     publish("test2", 2)
    #     publish("test3", 2)
    #     _start_num = 100 + 2.5 * 360 + 1
    #     publish("test1", 2, start_num=_start_num)
    #     _start_num = 100 + 2 * 360 + 1
    #     publish("test2", 2, start_num=_start_num)
    #     # 调用定时任务计算
    #
    #     cal()
    #
    #     assert cnc_5.query_production(_start_date, "test1") == 1621
    #     assert cnc_5.query_production(_start_date, "test2") == 1441
    #     assert cnc_5.query_production(_start_date, "test3") == 720


if __name__ == '__main__':
    # TestDataInput().test_1()
    pytest.main([__file__])
