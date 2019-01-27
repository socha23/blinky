from led import LED
from fire import Fire


class BaseMachine:
    def __init__(self):
        self.leds = []
        self.fires = []

    def add_led(self, pin, name):
        led = LED(pin, name)
        self.leds.append(led)
        return self

    def add_fire(self, pin_r, pin_y, name):
        fire = Fire("fire" + str(len(self.fires)), pin_r, pin_y, name)
        self.fires.append(fire)
        return self

    def led(self, pin):
        return next(x for x in self.leds if x.pin == pin)

    def fire(self, id):
        return next(x for x in self.fires if x.id == id)

    def state(self):
        return {
            'leds': [led.state() for led in self.leds],
            'fires': [fire.state() for fire in self.fires],
        }
