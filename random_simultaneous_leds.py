'''
Darryl Meyer
14 July 2015

Lights up multiple LEDs simultaneously in a random sequence (random groups).

'''

import RPi.GPIO as GPIO
import time
import sys
import random

def turn_on_LEDs(args):
	for i in args:
		try:
			GPIO.output(i, GPIO.HIGH) # HIGH = LED on
		except Exception as e:
			print("Could not light up LED at pin " + str(i))

def turn_off_LEDs(args):
	for i in args:
		try:
			GPIO.output(i, GPIO.LOW) # LOW = LED off
		except Exception as e:
			print("Could not turn off LED at pin " + str(i))
		
def setup_pins(args):
	GPIO.setmode(GPIO.BOARD)
	for i in args:
		try:
			GPIO.setup(i, GPIO.OUT)
		except Exception as e:
			print(str(i) + " is not a valid pin on the Raspberry Pi")

if len(sys.argv) > 3:
	steps = int(sys.argv[1])
	wait_time = float(sys.argv[2])
	number_pins = len(sys.argv) - 3
	pins = []
	
	# Create an array of the pin numbers
	for i in range(number_pins):
		try:
			pins.append(int(sys.argv[3 + i]))
		except Exception as e:
			print(str(sys.argv[3 + i]) + " is not a valid pin number")

	for j in range(steps):
		# random group size
		g = random.randint(1, len(pins) - 1)
		
		# group of pin numbers, sized g
		group = []
		
		for k in range(g):
			r = random.randint(0, len(pins) - 1)
			group.append(pins[r])
		
		setup_pins(group)
		turn_on_LEDs(group)
		time.sleep(wait_time)
		turn_off_LEDs(group)

	GPIO.cleanup()
else:
	print("Usage: sudo python random_simultaneous_leds.py <steps> <time> <pin 1> ... <pin n>")
