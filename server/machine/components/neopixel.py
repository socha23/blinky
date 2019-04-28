from machine.components.stub_aware import SourceMixin
from machine.effects.fire import fire_source
from machine.effects.rainbow import rainbow_source
from machine.components.component import Component

# don't delete this, it's used by evaluated code


class Neopixel(Component):
    def __init__(self, id, pix_from, num_pixels, name, neopixel_strip):
        Component.__init__(self, id, name)
        self._setting = 'rgb'
        self._setting_params = {"r": 0.5, "g": 0.5, "b": 0.5, "brightness": 0.5, "speed": 0.5, "intensity": 0.5, "body": ""}
        self._device = _NeopixelDevice(neopixel_strip, pix_from, num_pixels, self._param_generator("brightness"))
        self._effect_evaluator = Evaluator(num_pixels)

    def _turn_off(self):
        self._device.set_sources([constant_source(0, 0, 0) for _ in range(self._device.num_pixels)])

    def _current_value(self):
        return self._device.value

    def _turn_on_current_setting(self):
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
        self._device.set_sources([fire_source() for _ in range(self._device.num_pixels)])

    def _rgb(self):
        set_defaults(self._setting_params, {'r': 0.5, 'g': 0.5, 'b': 0.5})
        self._device.set_sources([constant_source(
            self._setting_params["r"],
            self._setting_params["g"],
            self._setting_params["b"]
        ) for _ in range(self._device.num_pixels)])

    def _rainbow(self):
        self._device.set_sources([rainbow_source(
                speed_generator=self._param_generator('speed'),
                offset=float(i) * 256 / self._device.num_pixels
            ) for i in range(self._device.num_pixels)])

    def _effect(self):
        self._effect_evaluator.body = self._setting_params["body"]
        self._device.set_sources([self._effect_evaluator.get_source() for _ in range(self._device.num_pixels)])


def set_defaults(params, defaults):
    for name, val in defaults.items():
        if name not in params:
            params[name] = val


def constant_source(r, g, b):
    while True:
        yield (r, g, b)


class Evaluator:
    def __init__(self, num_pixels):
        self._body = "(1, 1, 1)"
        self._num_pixels = num_pixels

    def get_source(self):
        r, g, b = self._eval_body()

        def generator():
            while True:
                yield (next(r), next(g), next(b))
        return generator()

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
        if isinstance(val, list):
            self._value = val
        else:
            self._value = [val for i in range(self.num_pixels)]
        self._apply()

    @property
    def num_pixels(self):
        return self._num_pixels

    def set_sources(self, sources):
        def generator():
            while True:
                yield [next(source) for source in sources]
        self.source = generator()
        self.value = next(self.source)
        self._apply()

    def _apply(self):
        for i in range(self.num_pixels):
            (r, g, b) = self._value[i]
            brightness = next(self._brightness_generator)
            self._strip.set_pixel(self.pix_from + i, (r * brightness, g * brightness, b * brightness))
