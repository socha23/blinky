import os

STUBS = "MOCK_BLINKY" in os.environ

if not STUBS:
    from gpiozero import PWMLED as RealPWMLED
    from gpiozero.mixins import SourceMixin as RealSourceMixin
    from my_machine.neopixel_strip import NeopixelStrip as RealNeopixelStrip


class PWMLEDMock:
    def __init__(self, pin):
        self._value = 0

    @property
    def value(self):
        return self._value

    def on(self):
        self._value = 1

    def off(self):
        self._value = 0

    def blink(self):
        self._value = 0.1

    def pulse(self):
        self._value = 0.3


PWMLED = PWMLEDMock if STUBS else RealPWMLED


class SourceMixinMock:
    def __init__(self):
        pass


SourceMixin = SourceMixinMock if STUBS else RealSourceMixin


class NeopixelStripMock:
    def __init__(self, num_pixels, *args, **kwargs):
        pass

    @property
    def value(self):
        return 0,0,0

    @value.setter
    def value(self, val):
        pass

    def set_pixel(self, idx, val):
        pass


NeopixelStrip = NeopixelStripMock if STUBS else RealNeopixelStrip
