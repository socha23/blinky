from gpiozero_ps.generators import constant


class TurnOnAndOffEffectMixin:
    def __init__(self):
        self._setting_params.update({
            "turn_on_effect": "none",
            "fade_in_duration": 0.5,

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



