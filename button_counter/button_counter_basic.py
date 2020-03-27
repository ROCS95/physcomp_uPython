'''
button_counter_basic.py
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)

counter = 0

while True:
    if not button.value():
        counter+=1
        msg = ' '.join(['counter is', str(counter)])
        print(msg)
    sleep_ms(20)

