from machine.components.led import LED
from machine.components.neopixel import Neopixel
from machine.components.stub_aware import NeopixelStrip


class _Machine:
    def __init__(self):
        self._store = None
        self._leds = []
        self._neopixels = []
        self._neopixel_strip = None
        self._componentsById = {}

    def initialize(self, store):
        self._store = store
        self._load_settings()

    def component(self, component_id):
        return self._componentsById[component_id]

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
        self._save_settings(component_id)

    def set_component_setting(self, component_id, setting, params):
        self.component(component_id).set_setting_and_params(setting, params)
        self._save_settings(component_id)

    def _save_settings(self, component_id):
        component = self.component(component_id)
        self._store.put("component_settings", component_id, component.save())

    def _load_settings(self):
        for component_id, component in self._componentsById.items():
            settings = self._store.get("component_settings", component_id)
            if settings is not None:
                component.load(settings)
                component.off()

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
