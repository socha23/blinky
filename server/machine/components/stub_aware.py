import os
import threading
import time
from gpiozero_ps.generators import constant, square, triangular

STUBS = "MOCK_BLINKY" in os.environ

TICKING_MOCKS = []



def tick():
    while True:
        for mock in TICKING_MOCKS:
            mock.tick()
        time.sleep(0.01)

if not STUBS:
    from gpiozero import PWMLED as RealPWMLED
    from gpiozero.mixins import SourceMixin as RealSourceMixin
    from machine.components.neopixel_strip import NeopixelStrip as RealNeopixelStrip
else:
    thread = threading.Thread(target=tick, daemon=True)
    thread.start()


class PWMLEDMock:
    def __init__(self, pin):
        self._value = 0
        self._source = constant(0)
        TICKING_MOCKS.append(self)

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
        self._source = None
        TICKING_MOCKS.append(self)

    @property
    def source(self):
        return self._source

    @source.setter
    def source(self, val):
        self._source = val

    def tick(self):
        if self._source is not None:
            self.value = next(self._source)


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
