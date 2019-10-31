'''
button_inc.py

note: no reset
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)

val = 0
inc = 0.5

while True:
    if not button.value():
        val+=inc
        print(val)
    sleep_ms(20)