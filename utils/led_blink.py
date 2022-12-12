from machine import Pin
import utime

led_onboard = Pin('LED', Pin.OUT)

while True:
    led_onboard.toggle()
    utime.sleep(1)

