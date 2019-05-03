from gpiozero_ps.generators import constant
from itertools import tee


BASE_SPEED = float(3)


def color_wheel(pos):
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = float(pos * 3 / 256)
        g = float((255 - pos*3) / 256)
        b = 0
    elif pos < 170:
        pos -= 85
        r = float((255 - pos*3) / 256)
        g = 0
        b = float(pos*3 / 256)
    else:
        pos -= 170
        r = 0
        g = float(pos*3 / 256)
        b = float((255 - pos*3) / 256)
    return r, g, b


def rainbow_source(speed_generator=constant(1), offset=0):
    pos = offset
    while True:
        yield(color_wheel(pos))
        pos = (pos + BASE_SPEED * next(speed_generator)) % 255


def rainbow_sources(speed_generator=constant(1), offset=0):
    s1, s2, s3 = tee(speed_generator, 3)
    return (
        rainbow_source_color("r", s1, offset),
        rainbow_source_color("g", s2, offset),
        rainbow_source_color("b", s3, offset)
    )


def rainbow_source_color(color, speed_generator=constant(1), offset=0):
    pos = offset
    while True:
        r, g, b = color_wheel(pos)
        if color == "r":
            yield  r
        elif color == "g":
            yield g
        elif color == "b":
            yield b
        pos = (pos + BASE_SPEED * next(speed_generator)) % 255

