from flask import Blueprint, jsonify
from machine import Machine

neopixels_api = Blueprint('neopixel api', __name__)

API_METHODS = ['GET', 'PUT']


def render_state():
    resp = jsonify(Machine.state())
    resp.status_code = 200
    return resp


@neopixels_api.route('/neopixel/<id>/on', methods=API_METHODS)
def on(id):
    Machine.neopixel(id).on()
    return render_state()

@neopixels_api.route('/neopixel/<id>/off', methods=API_METHODS)
def off(id):
    Machine.neopixel(id).off()
    return render_state()
