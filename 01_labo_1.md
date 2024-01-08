## Labo 1

### Installatie van Micropython

#### Wat is MicroPython

MicroPython is een **bootloader** en programmeer-omgeving om een beperkte versie van Python te runnen op **microcontrollers**.  

#### Wat is een microcontroller

MicroControllers zijn eigenlijk éénvoudige computers zonder besturingssysteem.  

#### Download MicroPython

Volg de installatie-instructies op https://docs.micropython.org/en/latest/esp32/tutorial/intro.html om MicroPython te installeren.  
Voor deze chip specifiek kan je direct navigeren naar https://micropython.org/download/esp32/ en daar de firmware downloaden.  
De rechtstreeks link om the downloaden te https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin

#### Installatie esptool.py

Bij de start van deze installatie moet je via Python de esptool installeren die je gaat toelaten van een firmware te installeren.  
Dit doe je best via de python-packager **pip**

~~~
pip install esptool
~~~

Als deze syntax niet werkt (als het pip-commando) kan je onderstaande syntax gebruiken.

~~~
python -m pip install esptool
~~~

Als deze éénmaal geïnstalleerd is moet je 2 commando's uitvoeren.  

~~~
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
~~~

#### Voor Windows-gebruikers

Let wel, deze instructies zijn voor Linux-machines, als je werkt met een Windows (het is je vergeven) dien je "/dev/ttyUSB0" te vervangen door de naam van de COM-poort waar je toestel is met aangesloten.

Dus stel dat je devices op Windows is gekoppeld op COM-poort COM4 gebruik je:

~~~
python -m esptool --port COM4 erase_flash
python -m esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
~~~

Om deze COM-poort te gebruiken ga In Windows 10 (of 11) ga je naar de device-manager gaan kijken om deze te vinden.  
Zie ook https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/establish-serial-connection.html voor meer duiding.

##### Voor Windows-gebruikers: stuurprogramma/driver niet beschikbaar...

Mocht deze device aangeven dat het stuurprogramma niet beschikbaar is mag je de driver downloaden te
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads


### Connecteren op MicroPython

Op een microcontroller connectoren met MicroPython start met het gebruik van de seriële console.  
Een courante tool om dit te doen is **Putty**, mocht je deze nog niet hebben geïnstalleerd kan je deze downloaden te https://www.putty.org/

Eénmaal gedownload stel je deze in om te connecteren om dezelfde poort die je gebruikte voor de esptool.py (in Linux dit was /dev/ttyUSB0 en op Windows de eerder vermelde COM-poort )

Connecteer hierop via Putty met baudrate 115200.  
Als je connecteert verkrijg je een seriele console

~~~python
>>> print("Hello World")
Hello World
>>>
~~~

### Oefening: Schrijf een loopje

Als de voorgaande test werkt schrijven we een loop die van 1 tem 10 telt.  

### Oefening: Ledje blinken

Connecteer led 2 een led in serie met een weerstand tussen 200 en 400 ohm  
Gebruik hiervoor https://docs.micropython.org/en/latest/esp8266/tutorial/pins.html


Speel met volgende code:

~~~python
>>> import machine
>>> led = machine.Pin(2, machine.Pin.OUT)
>>> led.value(1)
>>> led.value(0)
~~~

Uit de context zou moeten blijken wat beide acties doen.  
De functie time.sleep zorgt ervoor dat je code een gegeven aantal seconden wacht.  

~~~python
>>> import time
>>> time.sleep(1)
~~~

Kan je dit gebruiken om een **blinking led** te maken, die 20 maal blinkt?
Maak een **functie** waar je als **argument** het aantal keer aangeeft dat je led moet blinken.

### Installeer Thonny

Download Thonny te https://thonny.org/ en installeer.  
Thonny is een éénvoudige editor die het je toelaat direct op je programma direct op ESP32 te ontwikkelen.

Meer info vind je te https://microcontrollerslab.com/getting-started-thonny-micropython-ide-esp32-esp8266/  

Om Thonny the connecteren aan je esp:

* Ga naar Tools/Options
* Selecteer de tab interpreter
* Selecteer "MicroPython ESP32" als interpreter

Maak de voorgaande oefening en bewaar deze via Thonny op je esp32.

### WIFI Connecteren

Maak een WIFI-verbinding (password zie bord)
Gebruik hiervoor https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html als gids...
https://docs.micropython.org/en/latest/esp8266/tutorial/network_basics.html#configuration-of-the-wifi

~~~
>>>
>>> import network
>>> sta_if = network.WLAN(network.STA_IF)
>>> ap_if = network.WLAN(network.AP_IF)
>>> ap_if.active()
False
>>> sta_if.active(True)
True
>>> sta_if.ifconfig()
('0.0.0.0', '0.0.0.0', '0.0.0.0', '0.0.0.0')
>>> sta_if.connect("vul hier sid in","vul hier password in")
E (847905) wifi:sta is connecting, return error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
OSError: Wifi Internal Error
>>> sta_if.isconnected()
True
>>> sta_if.active()
True
>>> sta_if.ifconfig()
('10.20.226.104', '255.255.255.0', '10.20.226.204', '10.20.226.204')
>>>
~~~

### BMP280

Om te starten connecteer je de sensor op je ESP32, gebruik hiervoor de volgende mapping

* Vin met 3.3v
* Gnd met Gnd
* SCL met 22
* SDA met 21

Belangrijke tips:

* Zorg ervoor dat je nooit je elektronische schakeling wijzigt zolang je bordje "gepowered is"
* Als je je bordje ontkoppelt zorg dat je het onkoppelt aan de kant van je PC (om te vermijden dat je de usb-connector te veel belast)

Stap 1:  
Zet de file https://github.com/dafvid/micropython-bmp280/blob/master/bmp280.py via Thonny op je esp32 

Stap 2:

Probeer de volgende code-snippet uit via Thonny:

~~~python
import machine
from machine import I2C
from bmp280 import *
bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
bmp = BMP280(bus)
print(bmp.temperature)
~~~


## Labo 2

* Oefening per 2 personen
* Gebruik van Github
* Je programmeert samen alternerend van laptop

## Github

We gaan deze oefening documenteren in Github.
We gaan een README.md aanmaken en daar onze documentatie volgen.

### Github configureren

* Ga naar github.com
  * Maak een github-account aan
  * Maak een lege repository aan, noem deze IoTInPractice1

* Maak ssh-keys aan
  * Voor Windows volg tutorial op https://phoenixnap.com/kb/generate-ssh-key-windows-10
  * Voor Linux en Mac voor onderstaande functies uit

~~~
ssh-keygen -t rsa
cat ~/.ssh/id_rsa
~~~

### Keys configureren in github

* Copieer deze naar github
  * Click rechtsboven op "Your profile"
  * Ga naar "Settings/SSH and GPG Keys"
  * New ssh-key
  * Geef titel en copier de publieke key

### Opdracht 1: Loopje schrijven met BMP280

Zorg ervoor dat je een loop schrijft die:

* Elke 30 seconden de temperatuur uitleest
* Deze print op de console

### Opdracht 2: Koppel een LED

Voeg een led toe, zorg ervoor dat dez 



### Mosquitto installeren

Download en installeer, zie naar voor instructies https://mosquitto.org/download/

~~~
mosquitto_pub -t test -m "testje voor mqtt"
~~~

~~~
mosquitto_sub -v -t 'test'
~~~

### ESP32: MQTT

Laad de umqtt-library op je esp...
https://raw.githubusercontent.com/RuiSantosdotme/ESP-MicroPython/master/code/MQTT/umqttsimple.py


~~~python
MQTT_BROKER = '39.106.151.85' # replace with ip-address of your PC
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
mqttClient.connect()
mqttClient.publish("test","bqsfqsd".encode())
~~~

### Publish vanuit

~~~ python
MQTT_BROKER = '39.106.151.85' # replace with ip-address of your PC
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
mqttClient = MQTTClient(CLIENT_ID, MQTT_BROKER, keepalive=60)
mqttClient.connect()
mqttClient.publish("test", json.dumps({"temperature" : str(bmp.temperature)}).encode())
~~~


### Luisteren op je PC (deel 1)

~~~
mosquitto_sub -v -t 'test'
~~~

### Luisteren op je PC (deel 2) 

~~~
pip install paho-mqtt
~~~

~~~python
import paho.mqtt.client as mqttClient

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
        global Connected                #Use global variable
        Connected = True                #Signal connection 
        client.subscribe("#")
    else:
        print("Connection failed")
  
def on_message(client, userdata, message):
    print(message)

client = mqttClient.Client("ttn")
client.on_connect= on_connect
client.on_message= on_message 
~~~

