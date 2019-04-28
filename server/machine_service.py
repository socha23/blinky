from my_machine import Machine


def state():
    return Machine.state()


def fire_on(fire_id):
    Machine.fire(fire_id).on()


def fire_set_intensity(fire_id, intensity):
    Machine.fire(fire_id).intensity = intensity


def fire_off(fire_id):
    Machine.fire(fire_id).off()


def led_on(pin):
    Machine.led(pin).on()


def led_off(pin):
    Machine.led(pin).off()


def led_blink(pin):
    Machine.led(pin).blink()


def led_pulse(pin):
    Machine.led(pin).pulse()


def led_pwm(pin, val):
    Machine.led(pin).pwm(val)


def neopixel_on(id):
    Machine.neopixel(id).on()


def neopixel_off(id):
    Machine.neopixel(id).off()


def neopixel_brightness(id, brightness):
    Machine.neopixel(id).brightness = brightness


def neopixel_fire(id):
    Machine.neopixel(id).fire()


def neopixel_rgb(id, params):
    Machine.neopixel(id).rgb(params)


def neopixel_effect(id, params):
    Machine.neopixel(id).effect(params)


def neopixel_rainbow(id, params):
    Machine.neopixel(id).rainbow(params)
