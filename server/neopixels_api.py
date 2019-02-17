from flask import Blueprint, jsonify, request
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

@neopixels_api.route('/neopixel/<id>/fire', methods=API_METHODS)
def fire(id):
    Machine.neopixel(id).fire()
    return render_state()

@neopixels_api.route('/neopixel/<id>/rgb', methods=API_METHODS)
def rgb(id):
    params = request.get_json()
    Machine.neopixel(id).rgb(r=params['r'], g=params['g'], b=params['b'])
    return render_state()


@neopixels_api.route('/neopixel/<id>/rgb/<r>/<g>/<b>', methods=API_METHODS)
def rgb_manual(id, r, g, b):
    Machine.neopixel(id).rgb(r=float(r), g=float(g), b=float(b))
    return render_state()


@neopixels_api.route('/neopixel/<id>/brightness/<brightness>', methods=API_METHODS)
def brightness(id, brightness):
    Machine.neopixel(id).brightness = float(brightness)
    return render_state()
