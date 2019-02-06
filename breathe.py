'''
    breathe.py

    sourced from https://learn.adafruit.com/micropython-hardware-analog-i-o/pulse-width-modulation
'''

from time import sleep
from machine import Pin, PWM

pwm = PWM(Pin(27))
pwm.freq(60)

while True:
    for i in range(1024):
        if i == 0:
            print("inhale")
        pwm.duty(i)
        sleep(0.001)
    for i in range(1023, -1, -1):
        if i == 1023:
            print("exhale")
        pwm.duty(i)
        sleep(0.001)
