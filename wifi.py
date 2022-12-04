import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ssid","password")

time.sleep(5)
print(wlan.isconnected())

