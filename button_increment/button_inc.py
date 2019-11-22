'''
button_inc.py

note: no reset
'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)

buttonPress = False

val = 0
inc = 1
modeThreshold = 500
modeChange = False

while True:
    if button.value() and buttonPress == False:
        print("ready to count a button press")
    elif not button.value() and buttonPress == False:
        print("starting counter")
        val+=inc
        print(val)
        buttonPress = True
    elif not button.value() and buttonPress == True:
#         print("still counting")
        val+=inc
        print(val)
        if val >= modeThreshold and modeChange == False:
            print("inc increased!")
            sleep_ms(250)
            inc = 2
            modeChange = True
        elif val >=modeThreshold and modeChange == True:
#             print("MORE POINTS!")
            val+=inc
            print(val)
            if val == 1000:
                print("YOU WIN!")
                break
    elif button.value() and buttonPress == True:
        message = " ".join(["Final value is:",str(val)])
        print(message)
        sleep_ms(2000)
        print("CHANGE PLAYERS")
        sleep_ms(1000)
        val = 0
        buttonPress = False
    sleep_ms(20)