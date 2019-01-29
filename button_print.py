'''
button.py
'''

import machine
import time

button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)

while True:
    if not button.value():
        print('Button pressed!')
    time.sleep_ms(20)
