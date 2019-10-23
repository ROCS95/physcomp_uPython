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

button = Pin(12, Pin.IN, Pin.PULL_UP)

thresholdCrossed = False

print("STARTING!")

while True:
    print("ready to cross threshold!")
    sensor_val = pot.read()
    if sensor_val <= 512 and thresholdCrossed == False:
        print("crossed threshold!")
        led.value(1)
        thresholdCrossed = True
    elif thresholdCrossed == True:
        print( "DO SOMETHING ELSE!")
        if not button.value():
            print("BUTTON PRESSED!")
            thresholdCrossed = False
            led.value(0)
    else:
        led.value(0)
    sleep_ms(20)
