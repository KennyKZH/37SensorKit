from machine import Pin
import time

ledPins = [16,17,18]
leds = [Pin(ledPins[0],Pin.OUT),Pin(ledPins[1],Pin.OUT),Pin(ledPins[2],Pin.OUT)]
delay_t = 0.1 
while True: 
    for led in leds: 
        led.high() 
        time.sleep(delay_t) 
        led.low() 
        time.sleep(delay_t) 