'''
button_press_counter_cases_limit.py
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)
prev_val = button.value()
limit = 5
counter = 0
action = 0

while True:
    if not button.value() and button.value() != prev_val:
        counter += 1
        if counter == limit:
            print('limit reached, resetting!')
            counter = 0
            action = 0
        else:
            action = counter
    if action == 1:
        print('interaction 1 is happening now!')
    elif action == 2:
        print('interaction 2 is happening now')
    elif action == 3:
        print('interaction 3 is happening now')
    elif action == 4:
        print('interaction 4 is happening now')
    prev_val = button.value()
    sleep_ms(20)

