import time
from umqtt.simple import MQTTClient


mqtt_server = 'broker.hivemq.com'
client_id = 'bigles'
topic_pub = b'TomsHardware'
topic_msg = b'Movement Detected'

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()

try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
while True:
    if sensor.value() == 0:
        client.publish(topic_pub, topic_msg)
        time.sleep(3)
    else:
        pass