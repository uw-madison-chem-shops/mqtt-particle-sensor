import settings

import sys
import machine
from machine import Pin, I2C, SPI
import network
import time
import struct

import mqtt_as
mqtt_as.MQTT_base.DEBUG = True



from homie.constants import FALSE, TRUE, BOOLEAN, FLOAT, STRING
from homie.device import HomieDevice
from homie.node import HomieNode
from homie.property import HomieNodeProperty

from uasyncio import get_event_loop, sleep_ms


from hpm import Sensor


class ParticleSensor(HomieNode):

    def __init__(self, name="hpm", device=None):
        super().__init__(id="hpm", name=name, type="sensor")
        self.device = device
        self.sensor = Sensor()
        self.pm25 = HomieNodeProperty(
            id="pm25",
            name="pm25",
            unit="ppm",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.pm25)
        self.pm10 = HomieNodeProperty(
            id="pm10",
            name="pm10",
            unit="ppm",
            settable=False,
            datatype=FLOAT,
            default=0,
        )
        self.add_property(self.pm10)
        self.uptime = HomieNodeProperty(
            id="uptime",
            name="uptime",
            settable=False,
            datatype=STRING,
            default="PT0S"
        )
        self.add_property(self.uptime)
        self.ip = HomieNodeProperty(
            id="ip",
            name="ip",
            settable=False,
            datatype=STRING,
            default="",
        )
        self.add_property(self.ip)
        self.led = Pin(0, Pin.OUT)
        self.online_led = Pin(15, Pin.OUT)
        self.online_led.off()
        self.last_online = time.time()
        self.start = time.time()
        loop = get_event_loop()
        loop.create_task(self.update_data())

    async def update_data(self):
        # wait until connected
        for _ in range(60):
            await sleep_ms(1_000)
            if self.device.mqtt.isconnected():
                break
        # loop forever
        while True:
            while self.device.mqtt.isconnected():
                self.last_online = time.time()
                self.online_led.on()
                self.led.value(0)  # illuminate onboard LED
                measured = self.sensor.read()
                self.pm25.data = str(measured["pm25"])
                self.pm10.data = str(measured["pm10"])
                self.uptime.data = self.get_uptime()
                self.ip.data = network.WLAN().ifconfig()[0]
                self.led.value(1)  # onboard LED off
                await sleep_ms(15_000)
            while not self.device.mqtt.isconnected():
                if time.time() - self.last_online > 300:   # 5 minutes
                    machine.reset()
                self.online_led.off()
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
    homie = HomieDevice(settings)
    homie.add_node(ParticleSensor(device=homie))
    homie.run_forever()


if __name__ == "__main__":
    main()
