from machine.stub_aware import SourceMixin
from machine.fire import fire_source
from machine.rainbow import rainbow_source

#don't delete this, it's used by evaluated code
from gpiozero_ps.generators import *


class Neopixel(SourceMixin):
    def __init__(self, id, pix_from, num_pixels, name, neopixel_strip, *args, **kwargs):
        SourceMixin.__init__(self, *args, **kwargs)
        self.id = id
        self.name = name
        self.pix_from = pix_from
        self.num_pixels = num_pixels
        self._strip = neopixel_strip
        self._value = [(0, 0, 0) for _ in range(num_pixels)]
        self._effect_evaluator = Evaluator(num_pixels)
        self.source = None

        self._brightness = 1

        self._setting = ''
        self._setting_params = {}
        self._on = False

        self.rgb()
        self.off()

    @property
    def brightness(self):
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        self._brightness = brightness
        self._apply()

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
    def setting(self):
        return self._setting

    @setting.setter
    def setting(self, val):
        self._setting = val

    def on(self):
        self._on = True
        self._apply_current_setting()

    def off(self):
        self._on = False
        self._set_sources([constant_source(0, 0, 0) for _ in range(self.num_pixels)])

    def _apply_current_setting(self):
        if self.setting == "fire":
            self.fire(self._setting_params)
        elif self.setting == "rgb":
            self.rgb(self._setting_params)
        elif self.setting == "effect":
            self.effect(self._setting_params)
        else:
            raise Exception("Unknown setting: " + self.setting)

    def fire(self, params={}):
        self._set_setting('fire', [fire_source() for _ in range(self.num_pixels)], params)

    def rgb(self, params={}):
        set_defaults(params, {'r': 0.5, 'g': 0.5, 'b': 0.5})
        self._set_setting("rgb", [constant_source(params["r"], params["g"], params["b"]) for _ in range(self.num_pixels)], params)

    def rainbow(self, params={}):
        self._setting_params = params
        self._set_setting("rainbow", [rainbow_source(
                speed_generator=self._param_generator('speed'),
                offset=float(i) * 256 / self.num_pixels
            ) for i in range(self.num_pixels)], params)

    def effect(self, body):
        self._effect_evaluator.body = body
        self._set_setting("effect", [self._effect_evaluator.get_source() for _ in range(self.num_pixels)], {'body': body})

    def _set_setting(self, setting_name, value_sources, setting_params):
        self._on = True
        self.setting = setting_name
        self._set_sources(value_sources)
        self._setting_params = setting_params

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'on': self._on,
            'setting': self.setting,
            'params': self._setting_params,
            'brightness': self.brightness
        }

    def _set_sources(self, sources):
        def generator():
            while True:
                yield [next(source) for source in sources]
        self.source = generator()
        self.value = next(self.source)
        self._apply()

    def _apply(self):
        for i in range(self.num_pixels):
            (r, g, b) = self._value[i]
            self._strip.set_pixel(self.pix_from + i, (r * self.brightness, g * self.brightness, b * self.brightness))

    def _param_generator(self, name):
        while True:
            yield self._setting_params[name] if name in self._setting_params else 0


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


