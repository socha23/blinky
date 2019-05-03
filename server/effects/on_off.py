from gpiozero_ps.generators import triangular, gaussian, maxed, squared, constant, dense
from gpiozero_ps.gpiozero_generators import clamped, scaled, multiplied
from itertools import tee

TIME_FACTOR = 5  # time multiplier - to conserve processor, each value from sources is repeated TIME_FACTOR times


def turn_on_effect(source, params):
    return fade_in(source)


def turn_off_effect(source, params):
    return fade_out(source)


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

