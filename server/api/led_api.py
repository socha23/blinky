from flask import Blueprint, jsonify
from machine import Machine

led_api = Blueprint('led api', __name__)

API_METHODS = ['GET', 'PUT']


def render_state():
    resp = jsonify(Machine.state())
    resp.status_code = 200
    return resp


@led_api.route('/led/<pin>/on', methods=API_METHODS)
def on(pin):
    Machine.led(pin).on()
    return render_state()


@led_api.route('/led/<pin>/off', methods=API_METHODS)
def off(pin):
    Machine.led(pin).off()
    return render_state()


@led_api.route('/led/<pin>/blink', methods=API_METHODS)
def blink(pin):
    Machine.led(pin).blink()
    return render_state()


@led_api.route('/led/<pin>/pulse', methods=API_METHODS)
def pulse(pin):
    Machine.led(pin).pulse()
    return render_state()


@led_api.route('/led/<pin>/pwm/<val>', methods=API_METHODS)
def pwm(pin, val):
    Machine.led(pin).pwm(float(val))
    return render_state()
