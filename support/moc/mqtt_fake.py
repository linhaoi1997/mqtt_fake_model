import paho.mqtt.client as mqtt
import json
import time
from support.moc.data_format import Moc


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


def on_publish(client, userdata, mid):
    print("mid", str(mid), sep=" ,")


class MqttFake(object):

    def __init__(self, host, topic, port=1883, user=None, password=None):
        self.host = host
        self.port = port
        self.topic = topic
        self.client = mqtt.Client()
        self.client.connect(host, port)
        if user and password:
            self.client.username_pw_set(user, password)
        self.client.on_connect = on_connect
        self.client.on_message = on_message
        self.client.on_publish = on_publish
        self.moc = None

    def _publish(self, data):
        if not self.client.is_connected():
            self.client.connect(self.host, self.port)
        self.client.publish(self.topic, json.dumps(data))
        print(data)

    def add_moc(self, moc: Moc):
        self.moc = moc

    def publish(self, data=None):
        if data:
            self._publish(data)
        else:
            self._publish(self.moc.generate())

    def continue_publish(self, time_step=3):
        while True:
            self.publish()
            time.sleep(time_step)

    def public_time_slot(self, ts_name, start_date, end_date, time_step=40, is_millisecond=True):
        self.moc.add_rule(ts_name, "time_range", (start_date, end_date, time_step, is_millisecond))
        while True:
            try:
                self.publish()
                time.sleep(0.006)
            except StopIteration:
                print("发送完毕")
                break
        self.moc.add_rule(ts_name, "default", time.time)


if __name__ == '__main__':
    host = "192.168.1.5"
    topic = "bm/qs/012/data/post"
    m = MqttFake(host, topic)
    t = int(time.time()) + 3600 * 24
    while True:
        t = int(time.time()) + 3600 * 24
        # t += 100
        m.publish({"ts": t})
        time.sleep(3)
