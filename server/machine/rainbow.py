from gpiozero_ps.generators import constant

BASE_SPEED = float(20)


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
