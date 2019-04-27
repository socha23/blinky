from machine.stub_aware import PWMLED

class LED:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.led = PWMLED(pin)
        self.value = 1
        self.setting = 'off'
        self.off()

    def on(self):
        self.led.value = self.value
        self.setting = 'on'

    def off(self):
        self.led.off()
        self.setting = 'off'

    def blink(self):
        self.led.blink()
        self.setting = 'blink'

    def pulse(self):
        self.led.pulse()
        self.setting = 'pulse'

    def pwm(self, val):
        self.value = val
        self.led.value = val

    def state(self):
        return {
            'pin': self.pin,
            'name': self.name,
            'setting': self.setting,
            'value': self.value,
        }
