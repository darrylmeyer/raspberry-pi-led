# raspberry-pi-led

This repo contains some scripts I created for controlling LEDs with my Raspberry Pi.
It's just some basic stuff like turning an LED on for 1 second then turning it off again. It will get more complicated as I go along.

Explaination of the scripts in this repo:

## single_led.py

The default settings are to turn on an LED connected to pin 22 for 1 second then turn it off again.

### Usage
 To run this script enter into the terminal: `sudo python single_led.py`
 You can also scpecify the almount of time the LED stays on in seconds and the pin to use by entering: `sudo python single_led.py <time> <pin_number>`

## three_leds.py

It turns on and off 3 LEDs in sequence.

### Usage
 To run this script enter into the terminal: `sudo python three_leds.py`
 You can also scpecify the almount of time the LED stays on in seconds and the pin to use by entering: `sudo python single_led.py <time> <pin_1_number> <pin_2_number> <pin_3_number>`

## multiple_leds.py

It turns on and off multiple LEDs in sequence, as specified by command line arguments.

### Usage
 To run this script enter into the terminal: `sudo python multiple_leds.py <time> <pin 1> ... <pin n>`
 Where time is the amount of time each LED will be on for and pin 1 to pin n are the pin numbers of the LEDs.
 
# Thanks
Thanks to Jeremy Morgan for his tutorial and Python code – available [here](https://www.jeremymorgan.com/tutorials/raspberry-pi/how-to-blink-led-raspberry-pi-2/). It helped to get me started.
