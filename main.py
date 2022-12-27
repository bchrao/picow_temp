import machine, onewire, ds18x20
from time import sleep


ds_pin = machine.Pin(1)
 
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))
 
roms = ds_sensor.scan()
 
print('Found DS devices')
print('Temperature (°C)')
 
while True:
 
  ds_sensor.convert_temp()
 
  sleep(1)
 
  for rom in roms:
 
    print(ds_sensor.read_temp(rom))
 
  sleep(3)