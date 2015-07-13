
'''
Darryl Meyer
13 July 2015

Lights up multiple LEDs as specified by command line arguments

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

if len(sys.argv) > 2:
	wait_time = float(sys.argv[1])
	number_pins = len(sys.argv) - 2
	
	for i in range(number_pins):
		pin = int(sys.argv[2 + i])
	
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)

		activateLED(pin, wait_time)

	GPIO.cleanup()
else:
	print("Usage: sudo python multiple_leds.py <time> <pin 1> ... <pin n>")



