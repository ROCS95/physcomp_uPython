# digital in to pwm out

from machine import ADC, Pin, PWM
from time import sleep_ms

motorPin = Pin(21)
pwm = PWM(motorPin, freq=20000, duty=0)

button = Pin(12, Pin.IN, Pin.PULL_UP)

while True:
    if not button.value():
        print("Spin")
        pwm.duty(1023)
    else:
        print("Stop")
        pwm.duty(0)
    sleep_ms(20)
