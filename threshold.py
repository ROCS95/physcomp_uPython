# threshold.py

import machine
from time import sleep_ms

potPin = machine.Pin(34, machine.Pin.IN)

pot = machine.ADC(potPin)
pot.atten(machine.ADC.ATTN_11DB)
pot.width(machine.ADC.WIDTH_10BIT) # 0 - 1023

led = machine.Pin(15, machine.Pin.OUT)

while True:
    sensor_val = pot.read()
    if sensor_val >= 512:
        led.value(1)
    else:
        led.value(0)
    sleep_ms(20)
