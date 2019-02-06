'''
threshold.py
'''

from machine import ADC, Pin
from time import sleep_ms

potPin = Pin(34, Pin.IN)
led = Pin(27, Pin.OUT)

pot = ADC(potPin)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT) # 0 - 1023

while True:
  sensor_val = pot.read()
  if sensor_val >= 512:
    print("crossed threshold!")
    led.value(1)
  else:
    led.value(0)
  sleep_ms(20)
