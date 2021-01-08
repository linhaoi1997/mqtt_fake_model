from test_case.fake_attendance_data import BaseDataMaker
from support.graphql_tools.find_schema_path import find_schema
import datetime
import pytz


class CreateMemberRecord(BaseDataMaker):

    def __init__(self):
        super(CreateMemberRecord, self).__init__()
        self.query = find_schema('mutations', 'createMemberRecord')

    @staticmethod
    def make_variables(**kwargs):
        return {
            "memberRecord": {
                "member": {"id": kwargs["id"]},
                "start": kwargs["start"],
                "deviceUuid": "01a33e41-5d62-4667-80d0-f5ab144cc7eb",
                "accessType": "NORMAL",
                "identityType": "ID"
            }
        }

    def make_data(self, start_date: list, id=27):
        kwargs = {"id": id}
        for i in start_date:
            day = datetime.datetime.strptime(i, "%Y-%m-%d %H:%M:%S")
            co_zone = pytz.timezone("Pacific/Apia")
            day = co_zone.localize(dt=day)
            kwargs["start"] = day.timestamp() * 1000
            self.variables = self.make_variables(**kwargs)
            yield self.variables
            yield self.send_request()


if __name__ == "__main__":
    starts_date = [
        "2019-04-01 09:00:00", "2019-04-01 18:00:00",  # 正常考勤
        "2019-04-02 09:00:00", "2019-04-02 09:01:00", "2019-04-02 18:00:00",  # 打三次卡

        "2019-04-03 09:00:00", "2019-04-03 18:59:59",  # 工作日加班不足最小单位一小时
        "2019-04-04 09:00:00", "2019-04-04 19:00:00",  # 加班满一小时
        "2019-04-08 09:00:00", "2019-04-08 19:00:01",  # 加班满一小时多一秒

        "2019-04-05 08:00:00", "2019-04-05 08:59:59",  # 节假日加班不满一小时
        "2019-02-04 08:00:00", "2019-02-04 09:00:00",  # 节假日加班满一小时
        "2019-02-05 08:00:00", "2019-02-05 09:00:01",  # 节假日加班满一小时一秒

        "2019-04-06 08:00:00", "2019-04-06 08:59:59",  # 周末加班不满一小时
        "2019-04-07 08:00:00", "2019-04-07 09:00:00",  # 周末加班满一小时
        "2019-04-13 08:00:00", "2019-04-13 09:00:01",  # 周末加班满一小时1s

        "2019-04-09 09:00:59", "2019-04-09 18:00:00",  # 迟到59s不算迟到
        "2019-04-10 09:01:00", "2019-04-10 18:00:00",  # 迟到1min记录
        "2019-04-11 09:01:01", "2019-04-11 18:00:00",  # 迟到1min1s记录

        "2019-04-12 09:00:00", "2019-04-12 17:59:01",  # 早退59s不算迟到
        "2019-04-15 09:00:00", "2019-04-15 17:59:00",  # 早退1min记录
        "2019-04-16 09:00:00", "2019-04-16 17:58:59",  # 早退1min1s记录

        "2019-04-17 09:00:00",  # 打卡一次算未出勤
        # 18日不打卡算未出勤 "2019-04-18 09:00:00", "2019-04-18 17:58:59",
        "2019-04-19 09:00:00", "2019-04-19 20:00:00",  # 待增加
    ]
    # test = CreateMemberRecord()
    # for i in test.make_data(starts_date):
    #     print(i)
    # starts_date_2020=[i.replace('2019',"2020") for i in starts_date]
    starts_date_2020 = ["2020-05-12 09:01:00", "2020-05-12 18:00:00"]
    test = CreateMemberRecord()
    for i in test.make_data(starts_date_2020,29):
        print(i)