'''
button_press_counter.py
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)
prev_val = button.value()
counter = 0

while True:
    if not button.value() and button.value() is not prev_val:
        counter+=1
        msg = ' '.join(['Button pressed', str(counter), 'times!'])
        print(msg)
    prev_val = button.value()
    sleep_ms(20)
