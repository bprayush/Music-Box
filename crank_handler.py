import smbus


class CrankHandler:

    def __init__(self):
        self.address = 0x48
        self.A0 = 0x40
        self.bus = smbus.SMBus(1)

    def read(self):
        self.bus.write_byte(self.address, self.A0)
        value = self.bus.read_byte(self.address)
        return value
