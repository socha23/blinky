class TurnOnAndOffEffectMixin:
    def __init__(self):
        self._setting_params.update({
            "turn_on_effect": "none",
            "fade_in_duration": 1,

            "turn_off_effect": "none",
            "fade_out_duration": 1,
        })

    def _wrap_source_in_turn_on_effect(self, source):
        return fade_in(source)

    def _wrap_source_in_turn_off_effect(self, source):
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



