from machine.components.component import Component
from machine.components.mocks import PWMLED
from gpiozero_ps.generators import constant, triangular, square
from machine.components.tick_aware import SourceConsumer


class LED(Component, SourceConsumer):
    def __init__(self, id, pin, name):
        Component.__init__(self, id, name)
        SourceConsumer.__init__(self)
        self._setting = 'const'
        self._setting_params = {"brightness": 0.5}
        self._device = PWMLED(pin)

    def _turn_on(self):
        self._update_current_setting()

    def _turn_off(self, effect=True):
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
        if self.setting == "const":
            self._const()
        elif self.setting == "blink":
            self._blink()
        elif self.setting == "pulse":
            self._pulse()
        else:
            raise Exception("Unknown setting: " + self.setting)

    def _const(self):
        self.source = self._param_generator("brightness")

    def _blink(self):
        self.source = square(height=self._param_generator("brightness"))

    def _pulse(self):
        self.source = triangular(height=self._param_generator("brightness"))

