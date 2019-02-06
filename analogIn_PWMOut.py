# analog in to pwm out

from machine import ADC, Pin, PWM
from time import sleep_ms

ledPin = Pin(27)
potPin = Pin(34)

pot = ADC(potPin)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT) # 0 - 1023

pwm = PWM(Pin(27), freq=20000, duty=0)

while True:
    sensor_val = pot.read()
    print(sensor_val)
    pwm.duty(sensor_val)
    sleep_ms(20)
