import settings

import sys
import machine
from machine import Pin, I2C, WDT
import network
import time
import struct
#from adafruit_sgp30 import Adafruit_SGP30

import mqtt_as
mqtt_as.MQTT_base.DEBUG = True

# from bme280 import BME280 #imports BME class will have to do the same for arduino
from hpm import HPM
from sgp30 import SGP30

from homie.constants import FALSE, TRUE, BOOLEAN, FLOAT, STRING
from homie.device import HomieDevice
from homie.node import HomieNode
from homie.property import HomieNodeProperty

from uasyncio import get_event_loop, sleep_ms

class ParticleSensor(HomieNode):

    def __init__(self, name="hpm", device=None):
        super().__init__(id="hmp", name=name, type="sensor")
        self.device = device
        self.i2c = I2C(scl=Pin(5), sda=Pin(4))
        self.hpm = HPM(i2c=self.i2c)
        self.sgp30 = SGP30(self.i2c)
        self.sgp30.iaq_init()
        self.pm25 = HomieNodeProperty(
            id="pm25",
            name="PM2.5",
            unit="µg/m³",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.pm25)
        self.pm10 = HomieNodeProperty(
            id="pm10",
            name="PM1.0",
            unit="µg/m³",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.pm10)
        self.ec02 = HomieNodeProperty(
            id="ec02",
            name="eC02",
            unit="",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.ec02)
        self.tvoc = HomieNodeProperty(
            id="tvoc",
            name="TVOC",
            unit="",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.tvoc)
        self.uptime = HomieNodeProperty(
            id="uptime",
            name="uptime",
            settable=False,
            datatype=STRING,
            default="PT0S"
        )
        self.add_property(self.uptime)
        loop = get_event_loop()
        loop.create_task(self.update_data())
        self.led = Pin(0, Pin.OUT)
        #self.online_led = Pin(12, Pin.OUT)
        #self.online_led.off()
        self.last_online = time.time()
        self.start = time.time()

    async def update_data(self):
        # wait until connected
        for _ in range(60):
            await sleep_ms(1_000)
            if self.device.mqtt.isconnected():
                break
        # loop forever
        while True:
            while self.device.mqtt.isconnected():
                try:
                    self.last_online = time.time()
                    #self.online_led.on()
                    self.led.value(0)  # illuminate onboard LED
                    self.pm25.data = str(self.hpm.pm25)
                    self.pm10.data = str(self.hpm.pm10)
                    self.ec02.data = str(self.sgp30.eC02)
                    self.tvoc.data = str(self.sgp30.TVOC)
                    self.uptime.data = self.get_uptime()
                    self.led.value(1)  # onboard LED off
                    await sleep_ms(15_000)
                except Exception as ex:
                    print(ex)
                    continue
            while not self.device.mqtt.isconnected():
                if time.time() - self.last_online > 300:   # 5 minutes
                    machine.reset()
                #self.online_led.off()
                self.led.value(0)  # illuminate onboard LED
                await sleep_ms(100)
                self.led.value(1)  # onboard LED off
                await sleep_ms(1000)
            machine.reset()  # if lost connection, restart

    def get_uptime(self):
        diff = int(time.time() - self.start)
        out = "PT"
        # hours
        if diff // 3600:
            out += str(diff // 3600) + "H"
            diff %= 3600
        # minutes
        if diff // 60:
            out += str(diff // 60) + "M"
            diff %= 60
        # seconds
        out += str(diff) + "S"
        return out

def main():
    # homie
    print("homie main")
    homie = HomieDevice(settings)
    homie.add_node(ParticleSensor(device=homie))
    homie.run_forever()

if __name__ == "__main__":
    main()
