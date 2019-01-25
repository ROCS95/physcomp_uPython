'''
blink w/ if statement
'''

import machine
import time

led = machine.Pin(13, machine.Pin.OUT)

while True:
  if led.value() == 0:
    led.value(1)
  else:
    led.value(0)
  time.sleep(0.5)
