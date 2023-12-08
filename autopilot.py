from rc_car import gpiosetup, left_side_forward, right_side_forward, forward, stop
import RPi.GPIO as GPIO
from servo import setServoAngle
from cvcaptures import capture
from time import sleep


servo = 1
moveDelay = 1

setServoAngle(servo, 90)
stop()
sleep(2)
gpiosetup()

def right():
    right_side_forward()
    sleep(moveDelay)
    stop()

def left():
    left_side_forward()
    sleep(moveDelay)
    stop()


qrcheck = None
while True:
    if qrcheck != None:
        stop()
        setServoAngle(servo, 0)
        sleep(2)
        capture()
        setServoAngle(servo, 90)
        right()
    forward()

