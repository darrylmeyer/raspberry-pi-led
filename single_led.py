import RPi.GPIO as GPIO
import time
import sys

'''
Darryl Meyer
13 July 2015

Lights up a single LED, in my case a green LED on pin 22

'''

def activateLED(pin, wait_time):
	try:
		GPIO.output(pin, GPIO.HIGH) # HIGH = LED on
		time.sleep(wait_time)
		GPIO.output(pin, GPIO.LOW) # LOW = LED off
	except Exception as e:
		print("Could not light up LED", e)
		GPIO.output(pin, GPIO.LOW)
		
	return;

wait_time = float(sys.argv[1]) if len(sys.argv) > 1 else 2 
pin = int(sys.argv[2]) if len(sys.argv) > 2 else 22

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)

activateLED(pin, wait_time)

GPIO.cleanup()
