from gpiozero_ps.generators import triangular, gaussian, maxed, squared, constant, dense
from gpiozero_ps.gpiozero_generators import clamped, scaled, multiplied
from itertools import tee

TIME_FACTOR = 5  # time multiplier - to conserve processor, each value from sources is repeated TIME_FACTOR times


def scale_and_clamp(source, intensity, scale_from, scale_to):
    return clamped(multiplied(scaled(source, scale_from, scale_to, 0, 1), intensity), 0, 1)


def fire_source(intensity_generator=constant(1)):
    (r, g, b) = fire_sources(intensity_generator)
    return zip(r, g, b)


def fire_sources(intensity_generator=constant(1)):
    slow = squared(clamped(
        triangular(
            gaussian(40 / TIME_FACTOR, 10 / TIME_FACTOR),
            gaussian(30 / TIME_FACTOR, 10 / TIME_FACTOR),
            gaussian(0.7, 0.1))
        , 0, 1))

    fast = squared(clamped(
        triangular(
            gaussian(7 / TIME_FACTOR, 2 / TIME_FACTOR),
            gaussian(6 / TIME_FACTOR, 2 / TIME_FACTOR),
            gaussian(0.7, 0.1),
            gaussian(8 / TIME_FACTOR, 3 / TIME_FACTOR))
        , 0, 1))

    (intensity_r_f, intensity_g_f,) = tee(intensity_generator, 2)
    (slow_r, slow_g) = tee(slow, 2)
    (fast_r, fast_g) = tee(fast, 2)

    slow_r = scale_and_clamp(slow_r, constant(1), 0.2, 1)
    slow_g = scale_and_clamp(slow_g, constant(1), 0, 0.1)

    fast_r = scale_and_clamp(fast_r, intensity_r_f, 0.5, 1.5)
    fast_g = scale_and_clamp(fast_g, intensity_g_f, -0.2, 0.6)

    source_r = maxed(slow_r, fast_r)
    source_g = maxed(slow_g, fast_g)
    return dense(source_r, TIME_FACTOR), dense(source_g, TIME_FACTOR), constant(0)
