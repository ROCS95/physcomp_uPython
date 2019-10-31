'''
fade_out.py
'''

from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(27), freq = 20000, duty = 1023)

for i in range(1023, -1, -1):
    print(i)
    pwm.duty(i)
    sleep(0.01)

print("OFF!")

pwm.deinit()
