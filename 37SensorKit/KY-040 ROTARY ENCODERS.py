from machine import Pin
from time import sleep

SW = Pin(15, Pin.IN, Pin.PULL_UP)
DT = Pin(14, Pin.IN)      
CLK  = Pin(13, Pin.IN)    

valorAnterior = True
switchPresionado = False

while True:
     if valorAnterior != CLK.value():
         if CLK.value() == False:
             if DT.value() == False:
                 print("Manecillas antihorario")
                 sleep(1)
             else:
                 print("Manecillas horario")
                 sleep(1)
         valorAnterior = CLK.value()   
    
     if SW.value() == False and not switchPresionado:
         print("Switch presionado") 
         switch_presionado = True
     if SW.value() == True and switchPresionado:
         switch_presionado = False