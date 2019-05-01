import os
from machine.components.tick_aware import SourceConsumer


class PWMLEDMock:
    def __init__(self, _):
        self._value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        self._value = val


PWMLED = PWMLEDMock


class NeopixelStripMock(SourceConsumer):

    def __init__(self, num_pixels):
        SourceConsumer.__init__(self)
        self._value = [(0, 0, 0) for _ in range(num_pixels)]
        self._last_shown = None

        def generator():
            while True:
                yield self._value
        self.source = generator()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        # optimization so we don't call show() too often
        if val == self._last_shown:
            return
        self._last_shown = val[:]

    def set_pixel(self, idx, val):
        self._value[idx] = val


NeopixelStrip = NeopixelStripMock


if "MOCK_BLINKY" not in os.environ:
    from gpiozero import PWMLED as RealPWMLED
    PWMLED = RealPWMLED
    from machine.components.neopixel_strip import NeopixelStrip as RealNeopixelStrip
    NeopixelStrip = RealNeopixelStrip


