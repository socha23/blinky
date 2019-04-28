from my_machine import Machine


def state():
    return Machine.state()


def component_on(component_id):
    Machine.component(component_id).on()


def component_off(component_id):
    Machine.component(component_id).off()


def update_component_params(component_id, params):
    Machine.component(component_id).update_params(params)


def set_component_setting(component_id, setting, params):
    Machine.component(component_id).set_setting_and_params(setting, params)


def led_blink(pin):
    Machine.led(pin).blink()


def led_pulse(pin):
    Machine.led(pin).pulse()


def led_pwm(pin, val):
    Machine.led(pin).pwm(val)
