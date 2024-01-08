# Labo 1

## Installatie van Micropython

### Wat is MicroPython

MicroPython is een **bootloader** en programmeer-omgeving om een beperkte versie van Python te runnen op microcontrollers.  

### Wat is een microcontroller

MicroControllers zijn eigenlijk éénvoudige computers zonder besturingssysteem.

### Installatie van Micropython

Volg de installatie-instructies op https://docs.micropython.org/en/latest/esp32/tutorial/intro.html om MicroPython te installeren.
Voor deze chip specifiek kan je direct navigeren naar https://micropython.org/download/esp32/ en daar de firmware downloaden.
Je kan deze firmware direct downloaden te https://micropython.org/resources/firmware/esp32-20220618-v1.19.1.bin

Bij de start van deze installatie moet je via Python de esptool installeren die je gaat toelaten van een firmware te installeren.

~~~
pip install esptool
~~~

Als deze geinstalleerd is moet je 2 commando's uitvoeren
Voor linux is dit als volgt:

~~~
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180511-v1.9.4.bin
~~~

Voor Windows gebruik je:

~~~
python -m esptool --port COM4 erase_flash
python -m esptool --chip esp32 --port COM4 write_flash -z 0x1000 esp32-20220618-v1.19.1.bin
~~~

Je vervangt echter /dev/ttyUSB0 door de echte poortnaam (op Windows is dit een COMX-poort).
In Windows 10 moet je naar de device-manager gaan kijken om deze te vinden.

Mocht deze device aangeven dat het stuurprogramma niet beschikbaar is mag je de driver downloaden te
https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads

Connecteer vervolgens via Putty op de COM-poort met baudrate 115200 en schrijf een loop die van 1 tem 10 telt

## Oefening Ledje blinken

Connecteer led 2 een led in serie met een weerstand tussen 200 en 400 ohm  
Gebruik hiervoor https://docs.micropython.org/en/latest/esp8266/tutorial/pins.html

Speel met volgende code:

~~~
>>> import machine
>>> led = machine.Pin(2, machine.Pin.OUT)
>>> led.value(1)
>>> led.value(0)
~~~

Uit de context zou moeten blijken wat beide acties doen.  
De functie time.sleep zorgt ervoor dat je code een gegeven aantal seconden wacht.  

~~~
>>> import time
>>> time.sleep(1)
~~~

Kan je dit gebruiken om een blinking led te maken, die 20 maal blinkt?
Maak een functie waar je als argument het aantal keer aangeeft dat je led moet blinken.

## Installeer Thonny

Installeer Thonny en bewaar de functie van voorgaande oefening

## WIFI Connecteren

~~~
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

## BMP280

Zet de file https://github.com/dafvid/micropython-bmp280/blob/master/bmp280.py via Thonny op je esp32 en probeer de volgende sequentie uit

~~~
>>> import machine
>>> from machine import I2C
>>> bus = I2C(1, scl = machine.Pin(22), sda = machine.Pin(21))
>>> from bmp280 import *
>>> bmp = BMP280(bus)
>>> bmp.temperature
~~~
