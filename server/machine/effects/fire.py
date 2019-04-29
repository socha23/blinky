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

    slow_r = scale_and_clamp(slow_r, intensity_r_s, 0.3, 1.5)
    slow_g = scale_and_clamp(slow_g, intensity_g_s, 0, 0.2)

    fast_r = scale_and_clamp(fast_r, intensity_r_f, 0, 1.5)
    fast_g = scale_and_clamp(fast_g, intensity_g_f, 0, 0.6)

    source_r = maxed(slow_r, fast_r)
    source_g = maxed(slow_g, fast_g)
    return source_r, source_g, constant(0)
