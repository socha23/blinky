from machine.components.component import Component
from machine.components.stub_aware import PWMLED
from gpiozero_ps.generators import constant, triangular, square

class LED(Component):
    def __init__(self, id, pin, name):
        Component.__init__(self, id, name)
        self._setting = 'const'
        self._setting_params = {"brightness": 0.5}
        self._device = PWMLED(pin)

    def _turn_off(self):
        self._device.source = constant(0)

    def _current_value(self):
        return self._device.value

    def _turn_on_current_setting(self):
        if self.setting == "const":
            self._const()
        elif self.setting == "blink":
            self._blink()
        elif self.setting == "pulse":
            self._pulse()
        else:
            raise Exception("Unknown setting: " + self.setting)

    def _const(self):
        self._device.source = self._param_generator("brightness")

    def _blink(self):
        self._device.source = square(height=self._param_generator("brightness"))

    def _pulse(self):
        self._device.source = triangular(height=self._param_generator("brightness"))

