# kohler-mqtt-air-quality-sensor
This repository contains the current firmware, kicad diagram, and mounting plate.
The current state of the device is functional. The Arduino Micro communicates with the Honeywell Particle Sensor and sends that data over I2C to the ESP2866 through the logic level converter. And then the ESP8266 retrieves the data from the Arduino over I2C and connects to the MQTT server and publishes data.

The google sheet kohler-air-quality is up to date with hours and parts.
