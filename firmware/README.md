# mqtt-weather-station firmware

This project uses [micropython](https://micropython.org/), specifically [microhomie](https://github.com/microhomie/microhomie). Currently we build on microhomie-esp8266-v3.0.2, the binary is in the folder.

You must define the private information defined in `settings.py`. Copy `settings.py.example` to make a folder `settings.py` and define all relevant variables.

Run `flash.sh` to flash the board. You will need [esptool](https://github.com/espressif/esptool) and [ampy](https://github.com/scientifichackers/ampy).

We recommend an [FTDI Basic Breakout](https://www.sparkfun.com/products/9716) to physically program the ESP8266.
