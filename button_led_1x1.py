'''
button_led.py
'''

import machine
import time

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
led = machine.Pin(27, machine.Pin.OUT)

while True:
    if not button.value():
        led.value(1)
    else:
        led.value(0)
    time.sleep_ms(20)
