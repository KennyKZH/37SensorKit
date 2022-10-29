from machine import Pin
import utime

led_pins = [16,17] 
leds = [Pin(led_pins[0],Pin.OUT),Pin(led_pins[1],Pin.OUT)]
delay_t = 0.1 
while True: 
    for led in leds: 
        led.value(1) 
        utime.sleep_ms(1000)
        print("Led High")
        led.value(0) 
        utime.sleep_ms(1000)
        print("Led Low")