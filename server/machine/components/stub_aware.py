import os
import threading
import time
from gpiozero_ps.generators import constant, square, triangular

STUBS = "MOCK_BLINKY" in os.environ

MOCKED_LEDS = []


def tick():
    while True:
        for led in MOCKED_LEDS:
            led.tick()
        time.sleep(0.01)

if not STUBS:
    from gpiozero import PWMLED as RealPWMLED
    from gpiozero.mixins import SourceMixin as RealSourceMixin
    from my_machine.neopixel_strip import NeopixelStrip as RealNeopixelStrip
else:
    thread = threading.Thread(target=tick, daemon=True)
    thread.start()


class PWMLEDMock:
    def __init__(self, pin):
        self._value = 0
        self._source = constant(0)
        MOCKED_LEDS.append(self)

    @property
    def value(self):
        return self._value

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, source):
        self._source = source

    def tick(self):
        self._value = next(self._source)


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
        return 0, 0, 0

    @value.setter
    def value(self, val):
        pass

    def set_pixel(self, idx, val):
        pass


NeopixelStrip = NeopixelStripMock if STUBS else RealNeopixelStrip
