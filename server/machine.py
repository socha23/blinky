from led import LED


class Machine:
    def __init__(self):
        self.state = {'leds': {}}
        self.leds = {}

    def add_led(self, pin, name):
        self.leds[pin] = LED(pin, name)
        return self

    def led(self, pin):
        return self.leds[int(pin)]




