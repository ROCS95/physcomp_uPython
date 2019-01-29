'''
blink w/ if statement
'''

import machine
from time import sleep_ms

led = machine.Pin(13, machine.Pin.OUT)

while True:
    if led.value() == 0:
        led.value(1)
    else:
        led.value(0)
    sleep_ms(20)
