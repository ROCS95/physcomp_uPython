'''
button_led_1x2.py
1 input (SPST button or similar)
2 outputs (LEDs)
'''

import machine
from time import sleep_ms

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led1 = machine.Pin(13, machine.Pin.OUT)
led2 = machine.Pin(27, machine.Pin.OUT)

while True:
    if not button.value():
        led1.value(1)
        led2.value(0)
    else:
        led1.value(0)
        led2.value(1)
    sleep_ms(20)
