


### Opzetten van MQTT-broker

### Testen van MQTT-broker

~~~python
def send_mqtt_payload(host, topic, payload): 
    client = mqttClient.Client("clientid")
    client.connect(host, port=1883)
    client.publish(topic, payload)

send_mqtt_payload("localhost","test","greetings")
~~~

~~~python
import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
        client.subscribe("mytopic")
    else:
        print("Connection failed")
  
def on_message(client, userdata, message):
    print(userdata)
    print(f"Message received from {message.topic}: {message.payload}")
    
client = mqttClient.Client("demo")
client.on_connect= on_connect
client.on_message= on_message
client.connect("localhost", port=1883)
client.loop_start()        #start the loop
    
try:
    while True:
        time.sleep(1)
  
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
~~~

### Testen vanaf de ESP

~~~python
import network
import time
from umqtt.simple import MQTTClient
import machine
from machine import I2C
from bmp280 import *

def read_temperature():
    bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
    bmp = BMP280(bus)
    bmp.temperature

def connect(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid,password)
    time.sleep(2)

def send_mqtt_payload(host, clientid, topic, payload):
    client = MQTTClient(clientid, host)
    client.connect()
    client.publish(topic,payload)
~~~


### Oploaden vanaf je PC

~~~python
from ampy.files import Files
from ampy.pyboard import Pyboard

def push_file( port, name, content):
    try:
        board = Pyboard(port)
        files = Files(board)
        files.put(name, content)
        return files.ls()
    except:
        board.close()
~~~


~~~python
con.connect(ssid, password)
payload=json.dumps({"temperature" : str(con.read_temperature)}).encode()
con.send_mqtt_payload("192.168.0.148", "hello", "mytopic", "payload")
~~~

~~~
import json
import con

ssid="telenet-4C87FE9"
password="ZvutsBk36nrj"
con.connect(ssid, password)
payload=json.dumps({"temperature" : str(con.read_temperature)}).encode()
con.send_mqtt_payload("192.168.0.148", "hello", "mytopic", "payload")
~~~

import json
import con

ssid="vul in"
password="vul in"
con.connect(ssid, password)
payload=json.dumps({"temperature" : str(con.read_temperature)}).encode()
con.send_mqtt_payload("192.168.0.148", "hello", "mytopic", "payload")