'''
blink w/ if statement
'''

from machine import Pin
from time import sleep

led = Pin(15, Pin.OUT)

while True:
    if led.value() == 0:
        led.value(1)
    else:
        led.value(0)
    sleep(1)
