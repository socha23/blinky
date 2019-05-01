from gpiozero_ps.generators import constant
from machine.effects.fire import fire_sources
from machine.effects.rainbow import rainbow_sources
from machine.components.component import Component
from machine.components.tick_aware import SourceConsumer


class Neopixel(Component):
    def __init__(self, device_id, pix_from, num_pixels, name, neopixel_strip):
        Component.__init__(self, device_id, name)
        self._setting = 'rgb'
        self._sources = [(constant(0), constant(0), constant(0)) for _ in range(num_pixels)]
        self._setting_params = {"r": 0.5, "g": 0.5, "b": 0.5, "brightness": 0.5, "speed": 0.5, "intensity": 0.5, "body": ""}
        self._device = _NeopixelDevice(neopixel_strip, pix_from, num_pixels, self._param_generator("brightness"))
        self._num_pixels = num_pixels

    def _turn_off(self, effect=True):
        if effect:
            self._device.set_sources([self._turn_off_effect(r, g, b) for (r, g, b) in self._sources])
        else:
            self._device.set_sources([(constant(0), constant(0), constant(0)) for _ in range(self._num_pixels)])

    def _turn_on(self):
        self._do_update_settings()
        self._device.set_sources([self._turn_on_effect(r, g, b) for (r, g, b) in self._sources])

    def _current_value(self):
        return self._device.value

    def _update_current_setting(self):
        self._do_update_settings()
        self._device.set_sources(self._sources)

    def _do_update_settings(self):
        if self.setting == "fire":
            self._fire()
        elif self.setting == "rgb":
            self._rgb()
        elif self.setting == "rainbow":
            self._rainbow()
        else:
            raise Exception("Unknown setting: " + self.setting)

    def _fire(self):
        self._set_sources([fire_sources(self._param_generator("intensity")) for _ in range(self._num_pixels)])

    def _rgb(self):
        set_defaults(self._setting_params, {'r': 0.5, 'g': 0.5, 'b': 0.5})
        self._set_sources([(
            self._param_generator("r"), self._param_generator("g"), self._param_generator("b")
        ) for _ in range(self._num_pixels)])

    def _rainbow(self):
        self._set_sources([rainbow_sources(speed_generator=self._param_generator('speed')) for _ in range(self._num_pixels)])

    def _turn_off_effect(self, r, g, b):
        return fade_out(r), fade_out(g), fade_out(b)

    def _turn_on_effect(self, r, g, b):
        return fade_in(r), fade_in(g), fade_in(b)

    def _set_sources(self, sources):
        self._sources = sources


def set_defaults(params, defaults):
    for name, val in defaults.items():
        if name not in params:
            params[name] = val


def fade_in(source, duration=50):
    for i in range(duration):
        yield next(source) * i / duration
    while True:
        yield next(source)


def fade_out(source, duration=50):
    for i in range(duration):
        yield next(source) * (1 - i / duration)
    while True:
        yield 0


class _NeopixelDevice(SourceConsumer):
    def __init__(self, neopixel_strip, pix_from, num_pixels, brightness_generator):
        SourceConsumer.__init__(self)
        self._strip = neopixel_strip
        self.pix_from = pix_from
        self._num_pixels = num_pixels
        self._value = [(0, 0, 0) for _ in range(num_pixels)]
        self._brightness_generator = brightness_generator
        self.source = None

    @property
    def value(self):
        # list of rgb values
        return self._value

    @value.setter
    def value(self, val):
        brightness = next(self._brightness_generator)
        for i in range(self._num_pixels):
            r, g, b = val[i]
            self._value[i] = (r * brightness, g * brightness, b * brightness)
            self._strip.set_pixel(self.pix_from + i, self._value[i])

    def set_sources(self, sources):
        def generator():
            while True:
                yield [(next(r), next(g), next(b)) for (r, g, b) in sources]
        self.source = generator()
