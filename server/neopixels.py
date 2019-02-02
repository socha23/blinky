import board
import neopixel


class Neopixel:
    def __init__(self, id, num_pixels, name):
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
        self._pixel.fill(val)
        self._pixel.show()

    def on(self):
        self.value = (255, 255, 255)
        self.setting = 'on'

    def off(self):
        self.value = (0, 0, 0)
        self.setting = 'off'

    def fire(self):
        self.value = (255, 128, 0)
        self.setting = 'fire'

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'setting': self.setting,
            'brightness': self.brightness,
            'num_pixels': self.num_pixels,
        }
