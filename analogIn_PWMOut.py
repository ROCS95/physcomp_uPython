# analog in to pwm out

import machine
from time import sleep_ms

ledPin = machine.Pin(15)
potPin = machine.Pin(34)

pot = machine.ADC(potPin)
pot.atten(machine.ADC.ATTN_11DB)
pot.width(machine.ADC.WIDTH_10BIT) # 0 - 1023

pwm = machine.PWM(ledPin)
pwm.freq(100)

while True:
    sensor_val = pot.read()
    print(sensor_val)
    pwm.duty(sensor_val)

    sleep_ms(20)
