from machine.led import LED
from machine.fire import Fire
from machine.neopixels import Neopixel
from machine.stub_aware import NeopixelStrip

class BaseMachine:
    def __init__(self):
        self._leds = []
        self._fires = []
        self._neopixels = []
        self._neopixel_strip = None
        self._componentsById = {}

    def add_led(self, pin, name):
        led = LED(pin, name)
        self._leds.append(led)
        self._componentsById[pin] = led
        return self

    def led(self, pin):
        return self.component(pin)

    def add_fire(self, pin_r, pin_y, name):
        fire = Fire("fire" + str(len(self._fires)), pin_r, pin_y, name)
        self._fires.append(fire)
        self._componentsById[fire.id] = fire
        return self

    def fire(self, id):
        return self.component(id)

    def set_neopixel_strip(self, num_pixels):
        self._neopixel_strip = NeopixelStrip(num_pixels)

    def add_neopixel(self, name, pix_from, num_pixels):
        pixels = Neopixel("neopixel" + str(len(self._neopixels)), pix_from, num_pixels, name, self._neopixel_strip)
        self._neopixels.append(pixels)
        self._componentsById[pixels.id] = pixels
        return self

    def neopixel(self, id):
        return self.component(id)

    def component(self, id):
        return self._componentsById[id]

    def state(self):
        return {
            'leds': [led.state() for led in self._leds],
            'fires': [fire.state() for fire in self._fires],
            'neopixels': [pixels.state() for pixels in self._neopixels],
        }
