# analog in to pwm out

from machine import ADC, Pin, PWM
from time import sleep_ms

ledPin = Pin(15)
potPin = Pin(34)

pot = ADC(potPin)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT) # 0 - 1023

pwm = PWM(ledPin)
pwm.freq(100)

while True:
    sensor_val = pot.read()
    print(sensor_val)
    pwm.duty(sensor_val)

    sleep_ms(20)
