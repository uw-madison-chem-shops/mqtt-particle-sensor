from machine import UART


class Sensor(object):

    def __init__(self):
        self.ser = UART(0, 9600)
        self.ser.init(9600, bits=8, parity=None, stop=1)

    def read(self):
        self.ser.write("\x68\x01\x04\x93")  # message to read
        out = self.ser.read(32)
        pm25, pm10 = struct.unpack_from(">hh", out[6:10])
        return {"pm25":pm25, "pm10":pm10}
