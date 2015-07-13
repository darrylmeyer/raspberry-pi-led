# raspberry-pi-led

This repo contains some scripts I created for controlling LEDs with my Raspberry Pi.
It's just some basic stuff like turning an LED on for 1 second then turning it off again. It will get more complicated as I go along.

Explaination of the scripts in this repo:

## single_led.py

The default settings are to turn on an LED connected to pin 22 for 1 second then turn it off again.

### Usage
 To run this script enter into the terminal: sudo python single_led.py
 You can also scpecify the almount of time the LED stays on in seconds and the pin to use by entering: sudo python single_led.py <time> <pin_number>

## three_leds.py

It turn on and off 3 LEDs in sequence.



# Thanks
Thanks to Jeremy Morgan for his tutorial and Python code – available [here](https://www.jeremymorgan.com/tutorials/raspberry-pi/how-to-blink-led-raspberry-pi-2/). It helped to get me started.
