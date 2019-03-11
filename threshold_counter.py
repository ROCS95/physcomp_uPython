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
counter = 0
limit = 5

while True:
    current_val = pot.read()
    # val = ' '.join(["current val is", str(current_val)])
    # print(val)
    diff = current_val - prev_val
    if diff >= threshold:
        press = ' '.join(["diff is", str(diff), "trigger detected!" ])
        print(press)
        counter+=1
        current_count = ' '.join(["counter is", str(counter)])
        print(current_count)
        sleep_ms(500) # this is a hack but stops repeated counts
        if counter == limit:
            print("DONE!")
            # break # uncomment to break out of loop
            counter = 0 # uncomment to reset loop to 0
    else:
        diff = current_val - prev_val
        # print(diff)
    prev_val = current_val
    sleep_ms(20)
