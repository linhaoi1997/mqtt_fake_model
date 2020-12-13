import time
from collections import OrderedDict
import random
import datetime


class BaseMoc(object):
    def generate(self):
        pass

    def add_rule(self, name, rule_name, rule):
        pass


class Moc(BaseMoc):

    def __init__(self, _format):
        self._format = _format
        self._info = OrderedDict()
        self.json_handle()

    def json_handle(self):
        for key, value in self._format.items():
            self._info[key] = self._handle(value)

    @staticmethod
    def _handle(value):
        if isinstance(value, dict):
            return Moc(value)
        elif isinstance(value, list):
            return ListMoc(value)
        else:
            return SingleParam(value)

    def generate(self):
        r = {}
        for name, value in self._info.items():
            r[name] = value.generate()
        return r

    def add_rule(self, name, rule_name, rule):
        for key, value in self._info.items():
            if name == key:
                value.add_rule(rule_name, rule)
            elif isinstance(value, BaseMoc):
                value.add_rule(name, rule_name, rule)

    def add_rules(self, name_list: list, rule_name, rule):
        for name in name_list:
            self.add_rule(name, rule_name, rule)

    def set_default(self, name, rule):
        rule_name = "default"
        for key, value in self._info.items():
            if name == key:
                value.add_rule(rule_name, rule)
            elif isinstance(value, BaseMoc):
                value.add_rule(name, rule_name, rule)

    def set_defaults(self, name_list: list, rule):
        for name in name_list:
            self.set_default(name, rule)

    def import_defaults(self, defaults: dict):
        for key, value in defaults.items():
            if isinstance(key, list):
                self.set_defaults(key, value)
            else:
                self.set_default(key, value)

    def import_rules(self, rules):
        for rule in rules:
            if isinstance(rule[0], list):
                self.add_rules(*rule)
            else:
                self.add_rule(*rule)


class ListMoc(BaseMoc):
    def __init__(self, _format):
        self._format = _format
        self.key = []
        self.value = []
        self.sign = None
        for _dict in self._format:
            if "k" in _dict.keys():
                self.key.append(_dict.get("k"))
                self.value.append(Moc(_dict))
                self.sign = "v"

    def generate(self):
        return [i.generate() for i in self.value]

    def add_rule(self, name, rule_name, rule):
        if name in self.key:
            index = self.key.index(name)
            self.value[index].add_rule(self.sign, rule_name, rule)


class SingleParam(object):

    def __init__(self, value):
        self.param = BaseParam(value)

    def add_rule(self, rule_name, rule):
        param = self.param
        value = param.default
        if rule_name == "default":
            self.param = DefaultParam(value)
        elif rule_name == "increase":
            self.param = IncreaseParam(value)
            self.param.num = 0
        elif rule_name == "multiple":
            self.param = MultipleParam(value)
        elif rule_name == "take_turns":
            self.param = TakeTurnParam(value)
        elif rule_name == "random":
            self.param = RandomParam(value)
        elif rule_name == "time_range":
            self.param = TimeRangeParam(value)
        del param
        self.param.add_rule(rule)

    def generate(self):
        return self.param.generate()


class BaseParam(object):
    def __init__(self, value):
        self.num = 0
        self.rule = None
        self.default = value

    def add_rule(self, rule):
        self.rule = rule

    @staticmethod
    def execute_rule(value):
        return value

    def _generate(self):

        if callable(self.default):
            try:
                return int(self.default())
            except ValueError:
                return self.default()
        else:
            return self.default

    def generate(self):
        return self.execute_rule(self._generate())


class DefaultParam(BaseParam):
    def add_rule(self, rule):
        self.default = rule


class IncreaseParam(BaseParam):
    def execute_rule(self, value):
        if isinstance(self.rule, tuple):
            value = self.rule[0]
            step = self.rule[1]
            max_value = self.rule[2]
        else:
            max_value = 10000
            step = self.rule
        result = value + self.num * step
        self.num += 1
        if result >= max_value:
            self.num = 0
        return result


class MultipleParam(BaseParam):
    def execute_rule(self, value):
        return value * self.rule


class TakeTurnParam(BaseParam):
    """
    ([1, 2], 3) 从【1，2】轮换,生成三次参数轮换一次
    """

    def execute_rule(self, value):
        result = self.rule[0][self.num // self.rule[1] % len(self.rule[0])]
        self.num += 1
        return result


class RandomParam(BaseParam):
    """
    ([1, 2], "uniform") 在区间内的小数
    """

    def execute_rule(self, value):
        return getattr(random, self.rule[1])(self.rule[0][0], self.rule[0][1])


class TimeRangeParam(BaseParam):
    """
    (start_date,end_date,step,is_millisecond)
    """

    @staticmethod
    def make_date(time_str):
        return datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S").timestamp()

    def execute_rule(self, value):
        start = self.make_date(self.rule[0])
        end = self.make_date(self.rule[1])
        step = self.rule[2]
        is_millisecond = self.rule[3]
        result = start + self.num * step
        if is_millisecond:
            result *= 1000
            end *= 1000
        if result > end:
            raise StopIteration
        else:
            self.num += 1
            return result


if __name__ == '__main__':
    _test = {
        "ts": time.time,
        "params": {
            "status": "1",
            "e": 10,
            "ia": 1,
            "ib": 1,
            "ic": 1,
            "ua": 1,
            "ub": 1,
            "uc": 1,
            "test": [
                {"k": "name", "v": "lin"},
                {"k": "age", "v": 12}
            ]
            # "production": 10
        }
    }

    test = Moc(_test)
    assert test.generate()
    test.add_rule("ua", "multiple", 1000)
    assert test.generate()["params"]["ua"] == 1000
    test.add_rule("status", "default", 1000)
    assert test.generate()["params"]["status"] == 1000
    test.add_rule("e", "increase", 10)
    assert test.generate()["params"]["e"] == 10
    assert test.generate()["params"]["e"] == 20
    assert test.generate()["params"]["e"] == 30
    test.add_rule("ia", "random", ([2, 3], "randint"))
    assert test.generate()["params"]["ia"] in (2, 3)
    test.add_rule("ia", "random", ([2, 3], "uniform"))
    ia = test.generate()["params"]["ia"]
    assert type(ia) == float and 2 <= ia < 3
    test2 = Moc(_test)
    test2.add_rule("status", "take_turns", ([1, 2], 2))
    assert test2.generate()["params"]["status"] == 1
    assert test2.generate()["params"]["status"] == 1
    assert test2.generate()["params"]["status"] == 2
    assert test2.generate()["params"]["status"] == 2
    assert test2.generate()["params"]["status"] == 1
    test2.add_rule("ts", "time_range", ("2020-09-01 12:00:00", "2020-09-02 13:00:00", 10, True))
    ts1 = test2.generate()["ts"]
    while True:
        try:
            ts2 = test2.generate()["ts"]
            assert (ts2 - ts1) == (10 * 1000)
            assert 1598932800000 <= ts2 <= 1599022800000
            ts1 = ts2
        except StopIteration:
            break

    test2.add_rule("ts", "time_range", ("2020-09-01 12:00:00", "2020-09-02 13:00:00", 10, False))
    ts1 = test2.generate()["ts"]
    while True:
        try:
            ts2 = test2.generate()["ts"]
            assert (ts2 - ts1) == 10
            assert 1598932800 <= ts2 <= 1599022800
            ts1 = ts2
        except StopIteration:
            break

    test3 = Moc(_test)
    test3.add_rule("name", "default", "li")
    assert test3.generate()["params"]["test"][0]["v"] == "li"
    test3.add_rule("age", "increase", 2)
    assert test3.generate()["params"]["test"][1]["v"] == 12
    assert test3.generate()["params"]["test"][1]["v"] == 14
