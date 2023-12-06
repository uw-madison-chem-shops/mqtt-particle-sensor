from machine import I2C, Pin
import struct


class Sensor(object):

    def __init__(self):
        self.i2c = I2C(scl=Pin(5), sda=Pin(4))

    def read(self):
        out = self.i2c.readfrom(16, 4)
        pm25, pm10 = struct.unpack_from(">HH", out)
        print(pm25, pm10)
        return {"pm25":pm25, "pm10":pm10}
