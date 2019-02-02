from flask import Blueprint, jsonify
from machine import Machine

neopixels_api = Blueprint('neopixels api', __name__)

API_METHODS = ['GET', 'PUT']


def render_state():
    resp = jsonify(Machine.state())
    resp.status_code = 200
    return resp


@neopixels_api.route('/neopixels/<id>/on', methods=API_METHODS)
def on(id):
    Machine.neopixels(id).on()
    return render_state()

@neopixels_api.route('/neopixels/<id>/off', methods=API_METHODS)
def off(id):
    Machine.neopixels(id).off()
    return render_state()
