import network

#ssid="bvnetwerk"
#password="xLbCMeZtac"

def connect():
    ssid="telenet-4C87FE9"
    password="ZvutsBk36nrj"

    sta_if = network.WLAN(network.STA_IF)
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid,password)
    print(sta_if.ifconfig())
#('10.20.226.104', '255.255.255.0', '10.20.226.204', '10.20.226.204')
 