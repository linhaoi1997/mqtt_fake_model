from test_case.operation import all_gh, gh_004


class TestStatus:
    def test_status(self):
        # 第一个设备：开机待机轮换
        # 第二个设备：一直待机
        # 第三个设备：一直开机
        # 第四个设备： 开关机轮换
        all_gh.continue_publish()

    def test_time_less_now(self):
        # 传入时间戳比当前小，数据应该丢弃不应该有变化
        gh_004.pub_one_hour_ago()


if __name__ == '__main__':
    test = TestStatus()
    test.test_status()
