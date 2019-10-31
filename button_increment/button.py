'''
button.py
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
        print('Button pressed!')
    sleep_ms(20)