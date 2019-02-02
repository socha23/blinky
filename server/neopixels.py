import board
import neopixel
from gpiozero.mixins import SourceMixin
from fire import fire_source

class Neopixel(SourceMixin):
    def __init__(self, id, num_pixels, name, *args, **kwargs):
        SourceMixin.__init__(self, *args, **kwargs)
        self.id = id
        self.name = name
        self.num_pixels = num_pixels
        self._pixel = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)
        self._value = (0, 0, 0)
        self.setting = 'off'
        self.off()

    @property
    def brightness(self):
        return self._pixel.brightness

    @brightness.setter
    def brightness(self, brightness):
        self._pixel.brightness = brightness
        self._pixel.show()

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        print(val)
        if isinstance(val, list):
            for i in range(min(len(val), self.num_pixels)):
                (r, g, b) = val[i]
                self._pixel[i] = (int(r * 255), int(g * 255), int(b * 255))
        else:
            (r, g, b) = val
            self._pixel.fill((int(r * 255), int(g * 255), int(b * 255)))
        self._pixel.show()

    def on(self):
        self.value = (1, 1, 1)
        self.source = None
        self.setting = 'on'

    def off(self):
        self.value = (0, 0, 0)
        self.source = None
        self.setting = 'off'

    def fire(self):
        def generator():
            sources = [fire_source() for _ in range(self.num_pixels)]
            while True:
                yield [next(source) for source in sources]
        self.source = generator()
        self.setting = 'fire'

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'setting': self.setting,
            'brightness': self.brightness,
            'num_pixels': self.num_pixels,
        }
