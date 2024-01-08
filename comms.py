import network
import time
from umqtt.simple import MQTTClient

def connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid,password)
    time.sleep(2)

def send_mqtt_payload(host, clientid, topic, payload):
    client = MQTTClient(clientid, host)
    client.connect()
    client.publish(topic,payload)