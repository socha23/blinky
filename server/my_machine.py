from machine import Machine


class MyMachine(Machine):
    def __init__(self):
        Machine.__init__(self)
        self.add_led(24, "Czerwony")
        self.add_led(25, "Bialy")
