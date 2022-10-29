from machine import Pin
from time import sleep

led = Pin(14, Pin.OUT)    
boton = Pin(13, Pin.IN)  

while True:
  
  estado = boton.value()
  if estado == True:     
      led.value(0)           
  else:                      
      led.value(1)    