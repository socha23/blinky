import board
import neopixel
from machine.components.tick_aware import SourceConsumer


class NeopixelStrip(SourceConsumer):
    def __init__(self, num_pixels):
        SourceConsumer.__init__(self)
        self.num_pixels = num_pixels
        self._pixel = neopixel.NeoPixel(board.D18, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.GRB)
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

        for i in range(self.num_pixels):
            (r, g, b) = val[i]
            self._pixel[i] = (int(r * 255), int(g * 255), int(b * 255))
        self._pixel.show()

    def set_pixel(self, idx, val):
        self._value[idx] = val
