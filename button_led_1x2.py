'''
button_led_1x2.py
1 input (SPST button or similar)
2 outputs (LEDs)
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)
led1 = Pin(15, Pin.OUT)
led2 = Pin(27, Pin.OUT)

while True:
    if not button.value():
        led1.value(1)
        led2.value(0)
    else:
        led1.value(0)
        led2.value(1)
    sleep_ms(20)
