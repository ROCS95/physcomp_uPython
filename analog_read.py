# analog read

import machine
from time import sleep_ms

adc = machine.ADC(machine.Pin(34))
adc.atten(machine.ADC.ATTN_11DB)

while True:
  print(adc.read())
  sleep_ms(20)
