from gpiozero_ps.generators import constant
from machine.components.stub_aware import SourceMixin
from machine.effects.fire import fire_sources
from machine.effects.rainbow import rainbow_sources
from machine.components.component import Component

# don't delete this, it's used by evaluated code


class Neopixel(Component):
    def __init__(self, id, pix_from, num_pixels, name, neopixel_strip):
        Component.__init__(self, id, name)
        self._setting = 'rgb'
        self._sources = [(constant(0), constant(0), constant(0)) for _ in range(num_pixels)]
        self._setting_params = {"r": 0.5, "g": 0.5, "b": 0.5, "brightness": 0.5, "speed": 0.5, "intensity": 0.5, "body": ""}
        self._device = _NeopixelDevice(neopixel_strip, pix_from, num_pixels, self._param_generator("brightness"))
        self._effect_evaluator = Evaluator(num_pixels)
        self._num_pixels = num_pixels

    def _turn_off(self, effect=True):
        if effect:
            self._device.set_sources([(fade_out(r), fade_out(g), fade_out(b)) for (r, g, b) in self._sources])
        else:
            self._device.set_sources([(constant(0), constant(0), constant(0)) for _ in range(self._num_pixels)])

    def _turn_on(self):
        self._do_update_settings()
        self._device.set_sources([(fade_in(r), fade_in(g), fade_in(b)) for (r, g, b) in self._sources])

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
        elif self.setting == "effect":
            self._effect()
        else:
            raise Exception("Unknown setting: " + self.setting)

    def _fire(self):
        self._set_sources([fire_sources() for _ in range(self._device.num_pixels)])

    def _rgb(self):
        set_defaults(self._setting_params, {'r': 0.5, 'g': 0.5, 'b': 0.5})
        self._set_sources([(
            self._param_generator("r"), self._param_generator("g"), self._param_generator("b")
        ) for _ in range(self._device.num_pixels)])

    def _rainbow(self):
        self._set_sources([rainbow_sources(
                speed_generator=self._param_generator('speed'),
                offset=float(i) * 256 / self._device.num_pixels
            ) for i in range(self._device.num_pixels)])

    def _effect(self):
        self._effect_evaluator.body = self._setting_params["body"]
        self._set_sources([self._effect_evaluator.get_sources() for _ in range(self._device.num_pixels)])

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


class Evaluator:
    def __init__(self, num_pixels):
        self._body = "(1, 1, 1)"
        self._num_pixels = num_pixels

    def get_sources(self):
        r, g, b = self._eval_body()
        return r, g, b

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, val):
        self._body = val
        self._eval_body()

    def _eval_body(self):
        return eval(self._body)


class _NeopixelDevice(SourceMixin):
    def __init__(self, neopixel_strip, pix_from, num_pixels, brightness_generator):
        SourceMixin.__init__(self)
        self._strip = neopixel_strip
        self.pix_from = pix_from
        self._num_pixels = num_pixels
        self._value = [(0, 0, 0) for _ in range(num_pixels)]
        self._brightness_generator = brightness_generator

    @property
    def value(self):
        # list of rgb values
        return self._value

    @value.setter
    def value(self, val):
        brightness = next(self._brightness_generator)
        self._value = [(r * brightness, g * brightness, b * brightness) for (r, g, b) in val]
        self._apply()

    @property
    def num_pixels(self):
        return self._num_pixels

    def set_sources(self, sources):
        def generator():
            while True:
                yield [(next(r), next(g), next(b)) for (r, g, b) in sources]
        self.source = generator()
        self.value = next(self.source)
        self._apply()

    def _apply(self):
        for i in range(self.num_pixels):
            self._strip.set_pixel(self.pix_from + i, self._value[i])
