import board
import neopixel


class Neopixels:
    def __init__(self, id, num_pixels, name):
        self.id = id
        self.name = name
        self.num_pixels = num_pixels
        self.pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=False, pixel_order=neopixel.GRB)
        self.setting = 'off'
        self.off()

    def on(self):
        self.pixels.fill((255, 255, 255))
        self.pixels.show()
        self.setting = 'on'

    def off(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        self.setting = 'on'

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'setting': self.setting,
            'num_pixels': self.num_pixels,
        }
