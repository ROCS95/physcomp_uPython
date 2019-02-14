# digital in to pwm out

from machine import ADC, Pin, PWM
from time import sleep_ms

motorPin = Pin(21)
pwm = PWM(motorPin, freq=20000, duty=0)
led = Pin(27, Pin.OUT)

button = Pin(12, Pin.IN, Pin.PULL_UP)

led.value(1)

while True:
    if not button.value():
        print("Spin motor, LED off")
        pwm.duty(1023)
        led.value(0)
    else:
        print("Stop motor, LED on")
        pwm.duty(0)
        led.value(1)
    sleep_ms(20)
