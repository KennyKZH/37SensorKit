from machine import Pin
import time

ledPins = [16,17] 
leds = [Pin(ledPins[0],Pin.OUT),Pin(ledPins[1],Pin.OUT)] 
delay = 0.1 
while True: 
    for led in leds: 
        led.high() 
        time.sleep(delay) 
        led.low() 
        time.sleep(delay) 