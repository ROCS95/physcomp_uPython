'''
fade_in.py
'''

from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(27), freq = 20000, duty = 0)

for i in range(1024):
    print(i)
    pwm.duty(i)
    sleep(0.01)

print("100%")

pwm.deinit()
