#LED Pinout test

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

pinled = [17, 27, 22]
pinInput = [5, 6, 13, 12]

choice = 0

if(GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)):
    choice = 1

elif(GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)):
    choice = 2

elif(GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)):
    choice = 3

elif(GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)):
    choice = 4

if (int(choice) >= 1 and int(choice) <= 3):
    for i in range(int(choice)):
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], 1)

elif (int(choice) == 4):
    for i in range(3):
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], 0)

else:
    print ("Number out of range of LEDs")
    
GPIO.cleanup()
