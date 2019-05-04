from gpiozero_ps.generators import constant


class TurnOnAndOffEffectMixin:
    def __init__(self):
        self._setting_params.update({
            "turn_on_effect": "none",
            "fade_in_duration": 0.5,

            "turn_off_effect": "none",
            "fade_out_duration": 0.5,
        })

    def _wrap_source_in_turn_on_effect(self, source):
        effect = self._setting_params['turn_on_effect']
        if effect == 'fade_in':
            return fade_in(source, int(200 * self._setting_params['fade_in_duration']))
        else:
            return source

    def _wrap_source_in_turn_off_effect(self, source):
        effect = self._setting_params['turn_off_effect']
        if effect == 'fade_out':
            return fade_out(source, int(200 * self._setting_params['fade_out_duration']))
        else:
            return constant(0)


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



