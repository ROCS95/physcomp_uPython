'''
button_inc_reset3.py

'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)

buttonPress = False

val = 0
inc = 1
modeThreshold = 500
modeChange = False
win = 1000

while True:
    if button.value() and buttonPress == False:
        print("ready to count a button press")
    elif not button.value() and buttonPress == False:
        print("starting counter")
        val+=inc # this could also be written: val = val + inc
        print(val)
        buttonPress = True
    elif not button.value() and buttonPress == True:
        val+=inc
        print(val)
        if val >= modeThreshold and modeChange == False:
            print("inc increased!")
            sleep_ms(350)
            inc = 2
            modeChange = True
        elif val >= modeThreshold and modeChange == True:
            val+=inc
            print(val)
            if val == win:
                print("YOU WIN!")
                print("GOODBYE!")
                sleep_ms(350)
                break
    elif button.value() and buttonPress == True:
        message = " ".join(["final value is:", str(val)])
        print(message)
        sleep_ms(2000)
        print("RESET!")
        sleep_ms(350)
        buttonPress = False
        val = 0
        inc = 1
    sleep_ms(20)