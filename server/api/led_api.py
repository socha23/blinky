from flask import Blueprint
from api.main_api import render_state
from machine.machine import Machine

led_api = Blueprint('led api', __name__)

API_METHODS = ['GET', 'PUT']


@led_api.route('/led/<pin>/blink', methods=API_METHODS)
def blink(pin):
    Machine.led_blink(pin)
    return render_state()


@led_api.route('/led/<pin>/pulse', methods=API_METHODS)
def pulse(pin):
    Machine.led_pulse(pin)
    return render_state()


@led_api.route('/led/<pin>/pwm/<val>', methods=API_METHODS)
def pwm(pin, val):
    Machine.led_pwm(pin, float(val))
    return render_state()
