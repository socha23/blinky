import board
import neopixel
from gpiozero.mixins import SourceMixin


class NeopixelStrip(SourceMixin):
    def __init__(self, num_pixels, *args, **kwargs):
        SourceMixin.__init__(self, *args, **kwargs)
        self.num_pixels = num_pixels
        self._pixel = neopixel.NeoPixel(board.D18, num_pixels, brightness=1, auto_write=False, pixel_order=neopixel.GRB)
        self._value = [(0, 0, 0) for i in range(num_pixels)]

        def generator():
            while True:
                yield self._value
        self.source = generator()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        if isinstance(val, list):
            for i in range(min(len(val), self.num_pixels)):
                (r, g, b) = val[i]
                self._pixel[i] = (int(r * 255), int(g * 255), int(b * 255))
        else:
            (r, g, b) = val
            self._pixel.fill((int(r * 255), int(g * 255), int(b * 255)))
        self._pixel.show()

    def set_pixel(self, idx, val):
        self._value[idx] = val
