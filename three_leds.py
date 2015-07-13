import RPi.GPIO as GPIO
import time

'''
Darryl Meyer
13 July 2015

Lights up 3 LEDs in sequence, in my case a green LED on pin 22,
a red LED on pin 23 and a yellow LED on pin 24.

'''

green = 22
red = 23
yellow = 24
wait_time = 1


GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)

def activateLED( pin, delay ):
  GPIO.output(pin, GPIO.HIGH) # HIGH = LED on
  time.sleep(delay)
  GPIO.output(pin, GPIO.LOW) # LOW = LED off
  return;

activateLED(green,timedelay)
activateLED(yellow,timedelay)
activateLED(red,timedelay)

GPIO.cleanup() # close GPIO library
