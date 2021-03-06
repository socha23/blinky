from itertools import tee

from gpiozero_ps.generators import constant
import random
import math

class LightSourceMixin:
    def __init__(self):
        self._setting_params.update({
            "turn_on_effect": "none",
            "fade_in_duration": 0.5,
            "neon_flicker_turn_on_speed": 0.5,

            "additional_effect": "none",
            "neon_flicker_intensity": 0.5,
            "pulse_intensity": 0.5,
            "pulse_duration": 0.5,

            "turn_off_effect": "none",
            "fade_out_duration": 0.5,
        })

    def _wrap_source_in_turn_on_effect(self, source_or_sources):
        if type(source_or_sources) is tuple or type(source_or_sources) is list:
            return self._wrap_sources_in_turn_on_effect(source_or_sources)
        else:
            return self._wrap_sources_in_turn_on_effect([source_or_sources])[0]

    def _wrap_sources_in_turn_on_effect(self, sources):
        effect = self._setting_params['turn_on_effect']
        if effect == 'fade_in':
            return [fade_in(source, int(200 * self._setting_params['fade_in_duration'])) for source in sources]
        elif effect == 'neon_flicker':
            speed = self._setting_params['neon_flicker_turn_on_speed']
            intensity_generators = tee(neon_startup_flicker_intensity(speed), len(sources))
            return [multiply(sources[i], intensity_generators[i]) for i in range(len(sources))]
        else:
            return sources

    def _wrap_source_in_additional_effect(self, source_or_sources):
        if type(source_or_sources) is tuple or type(source_or_sources) is list:
            return self._wrap_sources_in_additional_effect(source_or_sources)
        else:
            return self._wrap_sources_in_additional_effect([source_or_sources])[0]

    def _wrap_sources_in_additional_effect(self, sources):
        effect = self._setting_params['additional_effect']
        if effect == 'neon_flicker':
            intensity = self._setting_params['neon_flicker_intensity']
            intensity_generators = tee(neon_flicker_intensity(intensity), len(sources))
            return [multiply(sources[i], intensity_generators[i]) for i in range(len(sources))]
        elif effect == 'pulse':
            intensity = self._setting_params['pulse_intensity']
            duration = self._setting_params['pulse_duration']
            intensity_generators = tee(pulse_intensity(intensity, duration), len(sources))
            return [multiply(sources[i], intensity_generators[i]) for i in range(len(sources))]
        else:
            return sources

    def _wrap_source_in_turn_off_effect(self, source_or_sources):
        if type(source_or_sources) is tuple or type(source_or_sources) is list:
            return self._wrap_sources_in_turn_off_effect(source_or_sources)
        else:
            return self._wrap_sources_in_turn_off_effect([source_or_sources])[0]

    def _wrap_sources_in_turn_off_effect(self, sources):
        effect = self._setting_params['turn_off_effect']
        if effect == 'fade_out':
            return [fade_out(source, int(200 * self._setting_params['fade_out_duration'])) for source in sources]
        else:
            return [constant(0) for _ in sources]


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


def multiply(source, intensity_generator):
    while True:
        yield next(intensity_generator) * next(source)


def neon_startup_flicker_intensity(speed):
    blink_time = 5
    pause_between_blinks = 3
    pause_between_series = 80
    pause_between_series_min = 35
    pause_between_series_decay = scale(speed, 0.4, 0.9)

    while pause_between_series >= pause_between_series_min:
        for _ in range(one_two_maybe_three()):
            for _ in range(blink_time):
                yield 1
            for _ in range(int(random.gauss(pause_between_blinks, pause_between_blinks / 3))):
                yield 0
        next_pause = int(random.gauss(pause_between_series, pause_between_series / 3))
        for _ in range(next_pause):
            yield 0
        pause_between_series = int(next_pause * pause_between_series_decay)
    while True:
        yield 1


def neon_flicker_intensity(intensity):
    blink_time = 5
    pause_between_blinks = 3
    pause_between_series = 600

    while True:
        next_pause = max(0, int(random.gauss(pause_between_series * (1 - intensity), pause_between_series * (1 - intensity) / 3)))
        for _ in range(next_pause):
            yield 1
        for _ in range(one_two_maybe_three()):
            for _ in range(blink_time):
                yield 0
            for _ in range(int(random.gauss(pause_between_blinks, pause_between_blinks / 3))):
                yield 1


def pulse_intensity(intensity, speed):
    base_speed = 0.1
    t = 0
    while True:
        t += scale(speed, 0.05, 0.7) * base_speed
        yield 1 - intensity / 2 + (math.sin(t) * intensity / 2)


def one_two_maybe_three():
    k10 = random.randrange(10)
    if k10 < 5:
        return 1
    elif k10 < 8:
        return 2
    else:
        return 3


def scale(val, result_from, result_to):
    return result_from + val * (result_to - result_from)
