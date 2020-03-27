'''
button.py
'''

from machine import Pin
import time

val = 0

button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
        print('Button pressed!')
        print("starting counter")
        val+=1
        print(val)
    time.sleep_ms(20)
