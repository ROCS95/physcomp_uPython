'''
button_counter.py
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)
prev_val = button.value()
limit = 5
counter = 0

while True:
    if not button.value() and button.value() != prev_val:
        counter += 1
        msg = ' '.join(['Button pressed', str(counter), 'times!'])
        print(msg)
        if counter == limit:
            print('limit reached!')
            counter = 0
    prev_val = button.value()
    sleep_ms(20)
