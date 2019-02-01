# analog read

from machine import ADC, Pin
from time import sleep_ms

adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)

while True:
  print(adc.read())
  sleep_ms(20)
