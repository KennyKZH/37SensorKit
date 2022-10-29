from machine import Pin
import utime

flame_sensor = Pin(16, Pin.IN)
utime.sleep(2)

while True:
   if flame_sensor.value() == 1:
       print("Fuego detectado")
       utime.sleep(3)
   else:
       print("No se a detectado fuego")
       utime.sleep(1)
utime.sleep(2)