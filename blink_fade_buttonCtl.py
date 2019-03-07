## launching multiple threads from button counts

import _thread as th
from time import sleep
from machine import Pin, PWM

# turns threads on or off
blink_running = True
fade_running = True

# sets up button counter
button = Pin(33, Pin.IN, Pin.PULL_UP)
prev_val = button.value()
limit = 5
counter = 0

# blink function
def blink(pin, secs, run):

    led = Pin(pin, Pin.OUT) # setup led pin

    while run():
        led.value(not led.value())
        sleep(secs)
    led.value(0) # turn off when while loop is not running

# fade function
def fade(pin, secs, run):
    delay = 0.025

    pwm = PWM(Pin(pin), freq=20000, duty=0)

    steps = int(round(1024/(secs / delay / 2)))
    # print(str(secs) + " " + str(steps) + " ")
    while run():
        for i in range(0,1024,steps):
            pwm.duty(i)
            sleep(delay)
        for i in range(1023, -1, (-1 * steps)):
            pwm.duty(i)
            sleep(delay)
    pwm.duty(0) # turn off when while loop is not running

# turn blink off
def blink_run():
    return blink_running

# turn fade off
def fade_run():
    return fade_running

print("Starting!")

# loop here (control flow controlled by button count)
while True:
    if not button.value() and button.value() != prev_val:
        counter += 1
        msg = ' '.join(['Button pressed', str(counter), 'times!'])
        print(msg)

        if counter == limit:
            print('limit reached')
            break
            # counter = 0
        elif counter == 1:
            print('blink 12!')
            th.start_new_thread(blink, (12, 0.1, blink_run))
        elif counter == 2:
            print('fade 27!')
            th.start_new_thread(fade, (27, 2, fade_run))
        elif counter == 3:
            print('turn off 12!')
            blink_running = False
        elif counter == 4:
            print('turn off 27!')
            fade_running = False

    prev_val = button.value()
    sleep(0.1)

print("Done!")
