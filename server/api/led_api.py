from flask import Blueprint
from api.main_api import render_state
from machine_service import led_blink, led_pulse, led_pwm

led_api = Blueprint('led api', __name__)

API_METHODS = ['GET', 'PUT']


@led_api.route('/led/<pin>/blink', methods=API_METHODS)
def blink(pin):
    led_blink(pin)
    return render_state()


@led_api.route('/led/<pin>/pulse', methods=API_METHODS)
def pulse(pin):
    led_pulse(pin)
    return render_state()


@led_api.route('/led/<pin>/pwm/<val>', methods=API_METHODS)
def pwm(pin, val):
    led_pwm(pin, float(val))
    return render_state()
