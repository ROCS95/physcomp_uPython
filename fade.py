''' fade.py

    sourced from https://learn.adafruit.com/micropython-hardware-analog-i-o/pulse-width-modulation
'''

from time import sleep
import machine

pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)

while True:
    for i in range(1024):
        pwm.duty(i)
        sleep(0.001)
    for i in range(1023, -1, -1):
        pwm.duty(i)
        sleep(0.001)
