from support.moc.data_format import Moc
from support.moc.mqtt_fake import MqttFake
from support.moc.delete import delete, CockpitDelete, warehouse_info
from support.moc.mock_database import PostgresConn
import threading
from fabric import Connection
import datetime
import time
import pendulum

TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def return_time(ts, tag="hour"):
    now = pendulum.from_timestamp(ts, tz="Asia/Shanghai")
    now_hour = now.start_of(tag)
    return now_hour.strftime(TIME_FORMAT)


def return_hour_time(ts):
    return return_time(ts, "hour")


def return_day_time(ts):
    return return_time(ts, "day")


def make_date(time_str):
    return datetime.datetime.strptime(time_str, TIME_FORMAT).timestamp()


def trigger_timing_mask(task, start_date, end_date):
    if "day" in task:
        time_slot = 3600 * 24
    else:
        time_slot = 3600
    start = make_date(start_date) + time_slot
    end = make_date(end_date) + time_slot
    identity = int(start)
    while identity + 1 <= end:
        ssh_execute(task, identity + 1)
        if "day" in task or "input-record" == task:
            identity += 3600 * 24
        else:
            identity += 3600
    ssh_execute(task, identity + 1)


def ssh_execute(task, ts):
    host = "192.168.1.5"
    conn = Connection(host, user="teletraan", connect_kwargs={"password": "teletraan"})
    command = "cd workspace/test; docker-compose exec -T" \
              " cockpit-schedule python -m app.commands.schedule {task} --ts {ts}".format(task=task, ts=ts)
    cockpit = CockpitDelete()
    if "day" in task:
        cockpit.delete_single_day_data(return_day_time(ts - 3600 * 24))
    elif "hour" in task:
        cockpit.delete_single_hour_data(return_hour_time(ts - 3600))
    elif "input-record" == task:
        cockpit.delete_input_data(return_day_time(ts - 3600 * 24))
    del cockpit
    conn.run(command)


def execute_now_mission():
    now = int(time.time()) + 3601
    ssh_execute("thing-hour-report", now)
    ssh_execute("alerts-task", now)
    now = int(time.time()) + 3600 * 24 + 1
    ssh_execute("thing-day-report", now)


class Equipment(object):
    def __init__(self, thing_id, company_id, host, topic, _format, config=None, rules=None):
        self.thing_id = thing_id
        self.company_id = company_id
        self.mqtt_fake = MqttFake(host, topic)
        self.moc = Moc(_format)
        self.mqtt_fake.add_moc(self.moc)
        if config:
            self.moc.import_defaults(config)
        if rules:
            self.moc.import_rules(rules)
        self.ts_name = None

    def __getattr__(self, item):
        try:
            result = getattr(self.mqtt_fake, item)
        except AttributeError:
            result = getattr(self.moc, item)
        return result

    def delete(self):
        delete(self.thing_id, self.company_id)

    def public_time_slot(self, start_date, end_date, time_step=120, is_millisecond=False):
        self.mqtt_fake.public_time_slot(self.ts_name, start_date, end_date, time_step, is_millisecond)

    def wait_until_warehouse_complete(self):
        warehouse = PostgresConn(warehouse_info)
        table = "thing_data_%s" % self.company_id
        query = "select timestamp from %s  where thing_id = %s order by timestamp desc limit 1" % (table, self.thing_id)
        f_result = warehouse.query(query)
        while True:
            time.sleep(3)
            b_result = warehouse.query(query)
            print(f_result, b_result, f_result == b_result)
            if b_result == f_result:
                break
            else:
                f_result = b_result

    def trigger_all_timing_mask(self, start_date, end_date):
        self.wait_until_warehouse_complete()
        print("执行任务")
        print("开始计算")
        trigger_timing_mask("alerts-task", start_date, end_date)
        trigger_timing_mask("thing-hour-report", start_date, end_date)
        trigger_timing_mask("thing-day-report", start_date, end_date)
        trigger_timing_mask("input-record", start_date, end_date)


class Equipments(object):
    def __init__(self, *args):
        self.equipments = []
        self.ts_name = args[0].ts_name
        for equipment in args:
            self.equipments.append(equipment)
        self._threads = []

    def publish(self, *args):
        self._threads = []
        for equipment in self.equipments:
            self._threads.append(threading.Thread(target=equipment.publish, args=args))
        self.start()

    def continue_publish(self, *args):
        self._threads = []
        for equipment in self.equipments:
            self._threads.append(threading.Thread(target=equipment.continue_publish, args=args))
        # self._threads.append(threading.Thread(target=self.continue_execute_mission()))
        self.start()

    def public_time_slot(self, *args):
        self._threads = []
        for equipment in self.equipments:
            self._threads.append(threading.Thread(target=equipment.public_time_slot, args=args))
        self.start()
        time.sleep(10)
        start_date = args[0]
        end_date = args[1]
        trigger_timing_mask("alerts-task", start_date, end_date)
        trigger_timing_mask("thing-hour-report", start_date, end_date)
        trigger_timing_mask("thing-day-report", start_date, end_date)

    def start(self):
        for mission in self._threads:
            mission.start()
        for mission in self._threads:
            mission.join()

    def delete(self):
        for equipment in self.equipments:
            equipment.delete()

    @staticmethod
    def continue_execute_mission(time_interval=200):
        while True:
            execute_now_mission()
            time.sleep(time_interval)


if __name__ == '__main__':
    execute_now_mission()
