import _thread as th
from time import sleep
from machine import Pin

blink1_running = True
blink2_running = True

def blink(pin, secs, run):

    led = Pin(pin, Pin.OUT) # setup pin

    while run():
        led.value(not led.value())
        sleep(secs)
    led.value(0) # turn off when while loop is not running

def blink_run1(): # keeps  track of whether blink is running or not
    return blink1_running

def blink_run2():
    return blink2_running

print("Start")

th.start_new_thread(blink, (12, 0.1, blink_run1))
th.start_new_thread(blink, (27, 0.5, blink_run2))

sleep(5)

print("stop")

blink1_running = False
blink2_running = False

print("done!")
