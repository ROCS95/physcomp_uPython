'''
button_led.py
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

while True:
    if not button.value():
        led.value(1)
    else:
        led.value(0)
    sleep_ms(20)
