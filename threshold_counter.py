'''
threshold_counter.py
'''

from machine import ADC, Pin
from time import sleep_ms

potPin = Pin(34, Pin.IN)

pot = ADC(potPin)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_10BIT) # 0 - 1023

threshold = 200

prev_val = pot.read()
prev_state = False
counter = 0
limit = 5

while True:
    current_val = pot.read()
    diff = current_val - prev_val
    if diff >= threshold and prev_state is False:
        press = ' '.join(["diff is", str(diff), "trigger detected!" ])
        print(press)
        counter+=1
        current_count = ' '.join(["num triggers:", str(counter)])
        print(current_count)
        prev_state = True
        if counter == limit:
            print("DONE!")
            break # uncomment to break out of loop
            counter = 0 # uncomment to reset loop to 0
    else:
        diff = current_val - prev_val
        # nopress = ' '.join(["diff is", str(diff), "no trigger!"])
        # print(nopress)
        prev_state = False
    prev_val = current_val
    sleep_ms(20)
