from machine import I2C
import time

# Arduino MICRO default address
HPM_I2C_ADDR = 0x0A


class Device:
    """Class for communication with I2C device.

    Reading and writing byte arrays from bus"""
    def __init__(self, address, i2c):
        #Create an instance of the I2C device at specified address
        self._address = address
        self._i2c = i2c

    def writeBus8(self, value):
        value = value
        self._i2c.writeto(self._address, value)

    def readByte(self):
        #Read an 8-bit value on the bus
        value = int.from_bytes(self._i2c.readfrom(self._address, 1), 'little') & 0xFF
        return value

    def readBytes(self, nBytes):
        value = self._i2c.readfrom(self._address, nBytes)
        return value

class HPM:
    def __init__(self, address=HPM_I2C_ADDR, i2c=None):
        # Create I2C device
        if i2c is None:
            raise ValueError('An I2C object is required.')
        self._device = Device(address, i2c)

    def read_pm(self):
        pmb = bytes(4)
        pmb = self._device.readBytes(4)
        return pmb

    def read_pm25(self):
        pmb = self.read_pm()
        pm25b = pmb[0:2]
        return int.from_bytes(pm25b, 'big')

    def read_pm10(self):
        pmb = self.read_pm()
        pm10b = pmb[2:4]
        return int.from_bytes(pm10b, 'big')

    @property
    def pm25(self):
        #Returns PM2.5
        pm25 = self.read_pm25()
        print("PM2.5: {}".format(pm25))
        return "{}".format(pm25)
    @property
    def pm10(self):
        #Returns PM1.0
        pm10 = self.read_pm10()
        print("PM1.0: {}".format(pm10))
        return "{}".format(pm10)
