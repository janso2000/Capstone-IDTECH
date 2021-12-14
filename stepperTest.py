import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(27,GPIO.OUT) # direction
GPIO.setup(17,GPIO.OUT) # step

step_count = 1000  # number of step to run  change this to change were it stops
delay = 0.0001

# drive motor counter clockwise number of steps set by step count
GPIO.output(27, GPIO.LOW)
print (" Drive CCW ", step_count ,"steps")
for x in range(step_count):
    GPIO.output(17, GPIO.HIGH)
    sleep(delay)
    GPIO.output(17, GPIO.LOW)
    sleep(delay)
    
# stop motor for 2 seconds    
print (" Stop")
sleep(2)

# drive motor clockwise number of steps set by step count
print (" Drive CW ", step_count ,"steps")
GPIO.output(27, GPIO.HIGH)
for x in range(step_count):
    GPIO.output(17, GPIO.HIGH)
    sleep(delay)
    GPIO.output(17, GPIO.LOW)
    sleep(delay)

# end of program
print (" End program")

GPIO.cleanup()