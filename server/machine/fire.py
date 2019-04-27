from machine.stub_aware import PWMLED
from gpiozero_ps.generators import triangular, gaussian, maxed, squared, constant
from gpiozero_ps.gpiozero_generators import clamped, scaled, multiplied
from itertools import tee


def scale_and_clamp(source, intensity, scale_from, scale_to):
    return clamped(multiplied(scaled(source, scale_from, scale_to, 0, 1), intensity), 0, 1)


def fire_source(intensity_generator=constant(1)):
    (r, g, b) = fire_sources(intensity_generator)
    return zip(r, g, b)

def fire_sources(intensity_generator=constant(1)):
    slow = squared(clamped(
        triangular(gaussian(70, 10), gaussian(50, 10), gaussian(0.7, 0.1))
       , 0, 1))

    fast = squared(clamped(
        triangular(gaussian(15, 4), gaussian(10, 3), gaussian(0.7, 0.1), gaussian(10, 3))
        , 0, 1))

    (intensity_r_s, intensity_g_s, intensity_r_f, intensity_g_f, ) = tee(intensity_generator, 4)
    (slow_r, slow_g) = tee(slow, 2)
    (fast_r, fast_g) = tee(fast, 2)

    slow_r = scale_and_clamp(slow_r, intensity_r_s, 0.2, 0.8)
    slow_g = scale_and_clamp(slow_g, intensity_g_s, -0.1, 0.3)

    fast_r = scale_and_clamp(fast_r, intensity_r_f, 0, 1.4)
    fast_g = scale_and_clamp(fast_g, intensity_g_f, -0.1, 0.5)

    source_r = maxed(slow_r, fast_r)
    source_g = maxed(slow_g, fast_g)
    return source_r, source_g, constant(0)


class Fire:
    def __init__(self, id, pin_red, pin_yellow, name):
        self.name = name
        self.id = id
        self.led_red = PWMLED(pin_red)
        self.led_yellow = PWMLED(pin_yellow)
        self.setting = 'off'
        self.__intensity = 1
        self.on()

    @property
    def intensity(self):
        return self.__intensity

    @intensity.setter
    def intensity(self, val):
        self.__intensity = max(0, min(1, val))

    def on(self):
        def intensity_generator():
            while True:
                yield self.intensity
        s_r, s_y = fire_sources(intensity_generator())
        self.led_red.source = s_r
        self.led_yellow.source = s_y
        self.setting = 'on'

    def off(self):
        self.led_red.source = None
        self.led_red.off()
        self.led_yellow.source = None
        self.led_yellow.off()
        self.setting = 'off'

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'setting': self.setting,
            'intensity': self.__intensity,
        }
