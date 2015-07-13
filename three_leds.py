'''
Darryl Meyer
13 July 2015

Lights up 3 LEDs in sequence, by default an LED on pin 22,
an LED on pin 23 and an LED on pin 24.

'''

import RPi.GPIO as GPIO
import time
import sys

def activateLED(pin, wait_time):
	try:
		GPIO.output(pin, GPIO.HIGH) # HIGH = LED on
		time.sleep(wait_time)
		GPIO.output(pin, GPIO.LOW) # LOW = LED off
	except Exception as e:
		print("Could not light up LED", e)
		GPIO.output(pin, GPIO.LOW)
		
	return;

wait_time = float(sys.argv[1]) if len(sys.argv) > 1 else 1 
pin_1 = int(sys.argv[2]) if len(sys.argv) > 2 else 22
pin_2 = int(sys.argv[3]) if len(sys.argv) > 3 else 24
pin_3 = int(sys.argv[4]) if len(sys.argv) > 4 else 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin_1, GPIO.OUT)
GPIO.setup(pin_2, GPIO.OUT)
GPIO.setup(pin_3, GPIO.OUT)

activateLED(pin_1, wait_time)
activateLED(pin_2, wait_time)
activateLED(pin_3, wait_time)

GPIO.cleanup() # close GPIO library
