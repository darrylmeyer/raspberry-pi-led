'''
Darryl Meyer
13 July 2015

Lights up multiple LEDs in a random sequence

'''

import RPi.GPIO as GPIO
import time
import sys
import random

def activateLED(pin, wait_time):
	try:
		GPIO.output(pin, GPIO.HIGH) # HIGH = LED on
		time.sleep(wait_time)
		GPIO.output(pin, GPIO.LOW) # LOW = LED off
	except Exception as e:
		print("Could not light up LED", e)
		GPIO.output(pin, GPIO.LOW)
		
	return;

if len(sys.argv) > 3:
	steps = int(sys.argv[1])
	wait_time = float(sys.argv[2])
	number_pins = len(sys.argv) - 3
	pins = []
	
	for i in range(number_pins):
		try:
			pins.append(int(sys.argv[3 + i]))
		except Exception as e:
			print(sys.argv[3 + i] + " is not a valid pin number")

	for j in range(steps):
		r = random.randint(0, len(pins) - 1)
	
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pins[r], GPIO.OUT)

		activateLED(pins[r], wait_time)

	GPIO.cleanup()
else:
	print("Usage: sudo python multiple_leds.py <steps> <time> <pin 1> ... <pin n>")




