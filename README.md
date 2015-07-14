# raspberry-pi-led

This repo contains some scripts I created for controlling LEDs with a Raspberry Pi.

Explaination of the scripts in this repo:

## single_led.py

The default settings are to turn on an LED connected to pin 22 for 1 second then turn it off.

### Usage
To run this script enter into the terminal: `sudo python single_led.py`
You can also scpecify the almount of time the LED stays on in seconds and the pin to use by entering: `sudo python single_led.py <time> <pin_number>`.

## three_leds.py

It turns on and off 3 LEDs in sequence. Default pins are 22, 23 and 24 and time is 1 second.

### Usage
To run this script enter into the terminal: `sudo python three_leds.py`
You can also scpecify the almount of time the LED stays on in seconds and the pin to use by entering: `sudo python single_led.py <time> <pin_1_number> <pin_2_number> <pin_3_number>`.

## multiple_leds.py

It turns on and off multiple LEDs in sequence, as specified by command line arguments.

### Usage
To run this script enter into the terminal: `sudo python multiple_leds.py <time> <pin 1> ... <pin n>`.
Where time is the amount of time an LED will be on for and pin 1 to pin n are the pin numbers of the LEDs.
 
## morse_code.py

Flashes a message in morse code using an LED.

### Usage
To run this script enter into the terminal: `sudo python morse_code.py <message> <pin>`.
Pin is by default 22. The message can include letters, numbers and spaces and should be enclosed in inverted commas if it contains more than one word.

## random_leds.py

Lights up multiple LEDs in a random sequence.

### Usage
To run this script enter into the terminal: `sudo python multiple_leds.py <steps> <time> <pin 1> ... <pin n>`.
Where steps is the number of LED on-off operations, time is the amount of time an LED will be on for and pin 1 to pin n are the pin numbers of the LEDs.

## Thanks
Thanks to Jeremy Morgan for his tutorial and Python code that helped to get me started – available [here](https://www.jeremymorgan.com/tutorials/raspberry-pi/how-to-blink-led-raspberry-pi-2/).
