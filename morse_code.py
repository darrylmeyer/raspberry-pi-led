
'''
Darryl Meyer
13 July 2015

Flashes a message in morse code using an LED.

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
	
def translate_message(message, pin):
	gap = 0.6 # space between letters
	for character in message:
		get_morse(character, pin)
		time.sleep(gap)
	
def get_morse(c, pin):
	dot = 0.2 # one unit
	dash = 0.6 # three units
	gap = 0.2 # space between parts of same letter, one unit
	space = 1.4 # space between words, seven units
	
	if (c == 'a'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'b'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'c'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'd'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'e'):
		activateLED(pin, dot)
	elif (c == 'f'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'g'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'h'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'i'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'j'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'k'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'l'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'm'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'n'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'o'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'p'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 'q'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'r'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 's'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == 't'):
		activateLED(pin, dash)
	elif (c == 'u'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'v'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'w'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'x'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'y'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == 'z'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == ' '):
		time.sleep(space)
	elif (c == '1'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == '2'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == '3'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == '4'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dash)
	elif (c == '5'):
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == '6'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == '7'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == '8'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == '9'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dot)
	elif (c == '0'):
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
		time.sleep(gap)
		activateLED(pin, dash)
	else:
		time.sleep(gap)	
		
if len(sys.argv) > 1:
	message = sys.argv[1]
	try:
		pin = int(sys.argv[2]) if len(sys.argv) > 2 else 22
		
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(pin, GPIO.OUT)

		translate_message(message, pin)

		GPIO.cleanup()
	except Exception as e:
		print("The second argument must be a valid pin number", e)
	
	
else:
	print("Usage: sudo python morse_code.py <message> <pin>")



