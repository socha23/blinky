from gpiozero import PWMLED


class LED:
    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.led = PWMLED(pin)
        self.setting = 'off'
        self.off()

    def on(self):
        self.led.on()
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
        self.led.value = val
        self.setting = 'pwm'
