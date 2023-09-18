# MQTT particle sensor

Designed to work with [mqtt.chem.wisc.edu](https://mqtt.chem.wisc.edu/).

## Repository

This is an open source hardware project licensed under the CERN Open Hardware Licence Version 2 - Permissive.
Please see the LICENSE file for the complete license.

## PCB

This PCB was designed using KiCAD version 7.
Refer to `mqtt_particle_sensor.pdf` for schematic.
PCB images generated with [tracespace](https://github.com/tracespace/tracespace) follow.

<img src="./mqtt_particle_sensor-.top.svg" width="100%"/>
<img src="./mqtt_particle_sensor-.bottom.svg" width="100%"/>

## Bill of Materials

| reference      | value         | manufacturer | part number       | price | vendors |
| :------------- | :------------ | :----------- | :---------------- | :---- | :------ |
| C1             | 1u            | Multicomp    | MC1206B105K500CT  | $0.10 | [Newark](https://www.newark.com/multicomp-pro/mc1206b105k500ct/ceramic-capacitor-1uf-50v-x7r/dp/06R4217?ost=mc1206b105k500ct)        |
| C2             | 1u            |  Multicomp   | MC1206B105K500CT  | $0.10 | [Newark](https://www.newark.com/multicomp-pro/mc1206b105k500ct/ceramic-capacitor-1uf-50v-x7r/dp/06R4217?ost=mc1206b105k500ct)        |
| C3             | 100u          | Illinois Capacitor|  107KXM025M| $0.25| [Newark](https://www.newark.com/cornell-dubilier/107kxm025m/aluminum-electrolytic-capacitor/dp/69K8200?ost=107kxm025m)        |
| C4             | 10u           |  Yageo       | CC1206KKX7R8BB106 | $0.25      | [Newark](https://www.newark.com/yageo/cc1206kkx7r8bb106/cap-10uf-25v-mlcc-1206-rohs-compliant/dp/26AK2052?st=cc1206kkx7r8bb106)      |
| C5             | 22u           | Murata Electronics| GRM31CC71C226ME11L| $0.75 | [Newark](https://www.newark.com/murata/grm31cc71c226me11l/cap-22uf-16v-mlcc-1206-rohs-compliant/dp/64AJ4421?ost=grm31cc71c226me11l)         |
| R1             | 470k          | 1206 1/4 1%  |                   |       |         |
| R2             | 1M            | 1206 1/4 1%  |                   |       |         |
| R3             | 1M            | 1206 1/4 1%  |                   |       |         |
| R4             | 4.7k          | 1206 1/4 1%  |                   |       |         |
| R5             | 4.7k          | 1206 1/4 1%  |                   |       |         |
| R6             | 1k            | 1206 1/4 1%  |                   |       |         |
| R7             | 1k            | 1206 1/4 1%  |                   |       |         |
| R8             | 4.7k          | 1206 1/4 1%  |                   |       |         |
| R9             | 4.7k          | 1206 1/4 1%  |                   |       |         |
| A1             | ESP8266 HUZZAH BREAKOUT BOARD | Adafruit | 2471 |  $10.00 | [Newark](https://www.newark.com/adafruit/2471/adafruit-huzzah-esp8266-breakout/dp/98Y0121?ost=esp8266+huzzah+breakout+board&cfm=true)        |
| U1             | Auto Reset Timer | Nexperia  | HEF4060BT,653 | $0.50      |[Newark](https://www.newark.com/nexperia/hef4060bt-653/ic-4000-locmos-smd-4060-soic16/dp/25M9620?st=hef4060bt,653)        |
| U2             | ATtiny85      | Microchip Technology| ATTINY85-20PU| $3.00       | [Newark](https://www.newark.com/microchip/attiny85-20pu/microcontroller-mcu-8-bit-attiny/dp/68T3808?ost=attiny85-20pu)|
| U3             | HPM Particle Sensor | Honeywell  | 	HPMA115S0-XXX| $63.75      |  [Newark](https://www.newark.com/honeywell/hpma115s0-xxx/particle-sensor-laser-uart-5v/dp/24AC9030?st=hpm%20particle%20sensor)       |
| D1             | LED (red)          |  Lite-On Inc. | LTST-C230KRKT | $0.25      | [Digikey](https://www.digikey.com/en/products/detail/liteon/LTST-C230KRKT/386857?s=N4IgTCBcDaIDIBUDKCC0BhMBmADAaQCU8EQBdAXyA)        |
| D2             | LED (green)         |  Lite-On Inc | LTST-C150KGKT| $0.25      | [Digikey](https://www.digikey.com/en/products/detail/liteon/LTST-C150KGKT/365085?s=N4IgTCBcDaIDIBUDKCC0BhAjAVgAwGkBxfBEAXQF8g)        |
| PS1            | Power         | CUI   | VXO7805-500-M-TR | $3.00      |[Newark](https://www.newark.com/cui/vxo7805-500-m-tr/dc-dc-converter-fixed-5v-rohs/dp/13AJ1536?ost=vxo7805-500-m-tr)        |
| J2             | Barrel Jack   |CUI |  PJ-002A  | $1.00      | [Digikey](https://www.digikey.com/en/products/detail/cui-devices/PJ-002A/96962)       |
| Q1             | 2N7000          | Diodes Inc.  | 2N7002K-7  |$0.25     |[Newark](https://www.newark.com/diodes-inc/2n7002k-7/mosfet-n-channel-60-v-800ma-sot/dp/25R5681?st=2n7002k-7)         |
| Q2             | 2N7000          | Diodes Inc.  | 2N7002K-7  |$0.25     |[Newark](https://www.newark.com/diodes-inc/2n7002k-7/mosfet-n-channel-60-v-800ma-sot/dp/25R5681?st=2n7002k-7)         |

## Firmware

This project uses [micropython](https://micropython.org/), specifically [microhomie](https://github.com/microhomie/microhomie).
Refer to the "firmware" directory in this repository for detailed instructions.

