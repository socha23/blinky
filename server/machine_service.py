from my_machine import Machine


def state():
    return Machine.state()


def component_on(id):
    Machine.component(id).on()


def component_off(id):
    Machine.component(id).off()


def fire_set_intensity(fire_id, intensity):
    Machine.fire(fire_id).intensity = intensity


def led_blink(pin):
    Machine.led(pin).blink()


def led_pulse(pin):
    Machine.led(pin).pulse()


def led_pwm(pin, val):
    Machine.led(pin).pwm(val)


def neopixel_brightness(id, brightness):
    Machine.neopixel(id).brightness = brightness


def neopixel_setting(id, setting, params):
    Machine.neopixel(id).set_setting_and_params(setting, params)
