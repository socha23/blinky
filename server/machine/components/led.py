from machine.components import Component, TurnOnAndOffEffectMixin, SourceConsumerMixin
from machine.components.mocks import PWMLED
from gpiozero_ps.generators import constant, triangular, square


class LED(Component, SourceConsumerMixin, TurnOnAndOffEffectMixin):
    def __init__(self, device_id, pin, name):
        Component.__init__(self, device_id, name)
        SourceConsumerMixin.__init__(self)
        TurnOnAndOffEffectMixin.__init__(self)
        self._setting = 'const'
        self._setting_params.update({"brightness": 0.5})
        self._device = PWMLED(pin)
        self._source = constant(0)

    def _turn_on(self, effect=True):
        self._do_update_settings()
        if effect:
            self.source = self._wrap_source_in_turn_on_effect(self._source)
        else:
            self.source = self._source

    def _turn_off(self, effect=True):
        if effect:
            self.source = self._wrap_source_in_turn_off_effect(self._source)
        else:
            self.source = constant(0)

    @property
    def value(self):
        return self._current_value()

    @value.setter
    def value(self, val):
        self._device.value = min(max(0, val), 1)

    def _current_value(self):
        return self._device.value

    def _update_current_setting(self):
        self._do_update_settings()
        self.source = self._source

    def _do_update_settings(self):
        if self.setting == "const":
            self._const()
        elif self.setting == "blink":
            self._blink()
        elif self.setting == "pulse":
            self._pulse()
        else:
            raise Exception("Unknown setting: " + self.setting)

    def _const(self):
        self._source = self._param_generator("brightness")

    def _blink(self):
        self._source = square(height=self._param_generator("brightness"))

    def _pulse(self):
        self._source = triangular(height=self._param_generator("brightness"))
