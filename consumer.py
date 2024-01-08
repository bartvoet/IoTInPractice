import paho.mqtt.client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
        client.subscribe("sensors/#")
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
