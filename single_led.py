import RPi.GPIO as GPIO
import time

'''
Darryl Meyer
13 July 2015

Lights up a single LED, in my case a green LED on pin 22

'''

green = 22 
wait_time = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(green, GPIO.OUT)

def activateLED(pin, wait_time):
  GPIO.output(pin, GPIO.HIGH) # HIGH = LED on
  time.sleep(delay)
  GPIO.output(pin, GPIO.LOW) # LOW = LED off
  return;

activateLED(green,wait_time)

GPIO.cleanup() # close GPIO library
