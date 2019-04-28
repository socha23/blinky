from machine.components.led import LED
from machine.components.neopixel import Neopixel
from machine.components.stub_aware import NeopixelStrip


class _Machine:
    def __init__(self):
        self._leds = []
        self._neopixels = []
        self._neopixel_strip = None
        self._componentsById = {}

    def component(self, id):
        return self._componentsById[id]

    def state(self):
        return {
            'leds': [led.state() for led in self._leds],
            'neopixels': [pixels.state() for pixels in self._neopixels],
        }

    def component_on(self, component_id):
        self.component(component_id).on()

    def component_off(self, component_id):
        self.component(component_id).off()

    def update_component_params(self, component_id, params):
        self.component(component_id).update_params(params)

    def set_component_setting(self, component_id, setting, params):
        self.component(component_id).set_setting_and_params(setting, params)

    def add_led(self, name, pin):
        led = LED("led" + str(pin), pin, name)
        self._leds.append(led)
        self._componentsById[led.id] = led
        return self

    def set_neopixel_strip(self, num_pixels):
        self._neopixel_strip = NeopixelStrip(num_pixels)

    def add_neopixel(self, name, pix_from, num_pixels):
        pixels = Neopixel("neopixel" + str(len(self._neopixels)), pix_from, num_pixels, name, self._neopixel_strip)
        self._neopixels.append(pixels)
        self._componentsById[pixels.id] = pixels
        return self


Machine = _Machine()
