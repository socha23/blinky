from led import LED


class Machine:
    def __init__(self):
        self.leds = {}
        self.leds_in_order = []

    def add_led(self, pin, name):
        led = LED(pin, name)
        self.leds_in_order.append(led)
        self.leds[pin] = led
        return self

    def led(self, pin):
        return self.leds[int(pin)]

    def state(self):
        return {
            'leds': [led.state() for led in self.leds_in_order]
        }