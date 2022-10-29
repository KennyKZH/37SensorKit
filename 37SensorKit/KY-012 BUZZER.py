from machine import Pin
import utime

rojo = Pin(18,Pin.OUT)
verde = Pin(19,Pin.OUT)
azul = Pin(20,Pin.OUT)
buzzer = Pin(21,Pin.OUT)

while True:
    rojo.off()
    verde.on()
    for i in range (3):
        buzzer.on()
        utime.sleep_ms(500)
        buzzer.off()
        utime.sleep_ms(500)
    verde.off()
    azul.on()
    for i in range (5):
        buzzer.on()
        utime.sleep_ms(100)
        buzzer.off()
        utime.sleep_ms(100)
    azul.off()
    rojo.on()
    utime.sleep_ms(3000)