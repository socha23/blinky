from gpiozero.mixins import SourceMixin
from fire import fire_source
from rainbow import rainbow_source

class Neopixel(SourceMixin):
    def __init__(self, id, pix_from, num_pixels, name, neopixel_strip, *args, **kwargs):
        SourceMixin.__init__(self, *args, **kwargs)
        self.id = id
        self.name = name
        self.pix_from = pix_from
        self.num_pixels = num_pixels
        self._strip = neopixel_strip
        self._value = [(0, 0, 0) for i in range(num_pixels)]
        self._brightness = 1
        self._setting = 'off'
        self._setting_params = {}
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
        self.rgb(1, 1, 1)
        self.setting = 'on'

    def off(self):
        self.rgb(0, 0, 0)
        self.setting = 'off'

    def fire(self):
        self.setting = 'fire'
        self._set_sources([fire_source() for _ in range(self.num_pixels)])
        self._setting_params = {}

    def rgb(self, r=1, g=1, b=1):
        self.setting = 'rgb'
        self._setting_params = {'r': r, 'g': g, 'b': b}
        self.source = None
        self.value = (r, g, b)

    def rainbow(self, speed=0.5):
        self._setting_params = {'speed': speed}
        if self.setting != 'rainbow':
            self.setting = 'rainbow'
            self._set_sources([rainbow_source(
                speed_generator=self._param_generator('speed'),
                offset=float(i) * 256 / self.num_pixels
            ) for i in range(self.num_pixels)])

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'setting': self.setting,
            'params': self._setting_params,
            'brightness': self.brightness
        }

    def _apply(self):
        for i in range(self.num_pixels):
            (r, g, b) = self._value[i]
            self._strip.set_pixel(self.pix_from + i, (r * self.brightness, g * self.brightness, b * self.brightness))

    def _set_sources(self, sources):
        def generator():
            while True:
                yield [next(source) for source in sources]
        self.source = generator()

    def _param_generator(self, name):
        while True:
            yield self._setting_params[name]
