#LED Pinout test

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

pins = [17 , 27, 22]

choice = input("Enter No between 1-3 for LEDs: ")

if (int(choice) >= 1 and int(choice) <= 3):
    for i in range(int(choice)):
        GPIO.setup(pins[i], GPIO.OUT)
        GPIO.output(pins[i], 1)
        time.sleep(0.5)

else:
    print ("Number out of range")
    
GPIO.cleanup()
