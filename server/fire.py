from gpiozero import PWMLED
from gpiozero_ps.generators import triangular, gaussian, maxed, squared
from gpiozero.tools import clamped, scaled
from itertools import tee


def fire_sources():
    slow = clamped(scaled(
        triangular(gaussian(30, 5), gaussian(30, 5), gaussian(0.7, 0.1)),
        0.1, 0.5, 0, 1), 0, 1)

    fast = clamped(triangular(gaussian(6, 2), gaussian(2, 1), gaussian(0.8, 0.06), gaussian(5, 5)), 0, 1)
    (fastR, fastY) = tee(fast, 2)

    source_r = squared(maxed(slow, fastR))
    source_y = squared(scaled(fastY, 0, 0.2, 0, 1))
    return source_r, source_y


class Fire:
    def __init__(self, id, pin_red, pin_yellow, name):
        self.name = name
        self.id = id
        self.led_red = PWMLED(pin_red)
        self.led_yellow = PWMLED(pin_yellow)
        self.setting = 'off'
        self.on()

    def on(self):
        s_r, s_y = fire_sources()
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
        }
