from random import gauss


def _value(numerOrGenerator):
    if isinstance(numerOrGenerator, float) or isinstance(numerOrGenerator, int):
        return numerOrGenerator
    else:
        return next(numerOrGenerator)


def gaussian(mu, sigma):
    while True:
        yield gauss(mu, sigma)


def maxed(*values):
    for v in zip(*values):
        yield max(v)


def squared(values):
    for v in values:
        yield v * v


def constant(value):
    while True:
        yield value


def from_callback(method):
    while True:
        yield method()


def triangular(ascent=100, descent=100, height=1, pause=0):
    value = 0
    while True:
        height_val = max(0, float(_value(height)))
        ascent_val = max(0, int(_value(ascent)))
        descent_val = max(0, int(_value(descent)))
        pause_val = max(0, int(_value(pause)))
        for _ in range(0, ascent_val):
            value += (height_val / ascent_val)
            yield value
        for _ in range(0, descent_val):
            value -= (height_val / descent_val)
            yield value
        value = 0
        for _ in range(0, pause_val):
            yield 0


def square(height=1, duration=100, pause=100):
    while True:
        height_val = max(0, float(_value(height)))
        duration_val = max(0, int(_value(duration)))
        pause_val = max(0, int(_value(pause)))
        for _ in range(0, duration_val):
            yield height_val
        for _ in range(0, pause_val):
            yield 0


def dense(generator, factor=2):
    while True:
        val = next(generator)
        for _ in range(factor):
            yield val
