'''
Darryl Meyer
14 July 2015

Lights up multiple LEDs simultaneously.

'''

import RPi.GPIO as GPIO
import time
import sys

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

if len(sys.argv) > 2:
	wait_time = float(sys.argv[1])
	number_pins = len(sys.argv) - 2
	pins = []
	
	for i in range(number_pins):
		try:
			pins.append(int(sys.argv[2 + i]))
		except Exception as e:
			print(str(sys.argv[2 + i]) + " is not a valid pin number")

	setup_pins(pins)
	turn_on_LEDs(pins)
	time.sleep(wait_time)
	turn_off_LEDs(pins)

	GPIO.cleanup()
else:
	print("Usage: sudo python simultaneous_leds.py <time> <pin 1> ... <pin n>")
