'''
button_inc_reset.py

'''

from machine import Pin
from time import sleep_ms

button = Pin(12, Pin.IN, Pin.PULL_UP)

buttonPress = False

val = 0
inc = 1

while True:
    if button.value() and buttonPress == False:
        print("ready to count a button press")
    elif not button.value() and buttonPress == False:
        print("starting counter")
        val+=inc
        print(val)
        buttonPress = True
    elif not button.value() and buttonPress == True:
        val+=inc
        print(val)
    elif button.value() and buttonPress == True:
        message = " ".join(["final value is:", str(val)])
        print(message)
        sleep_ms(2000)
        print("RESET!")
        sleep_ms(350)
        buttonPress = False
        val = 0
    sleep_ms(20)