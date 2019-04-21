from flask import Blueprint, jsonify, request, make_response
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


@neopixels_api.route('/neopixel/<id>/brightness/<brightness>', methods=API_METHODS)
def brightness(id, brightness):
    Machine.neopixel(id).brightness = float(brightness)
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


@neopixels_api.route('/neopixel/<id>/effect', methods=API_METHODS)
def effect(id):
    params = request.get_json()
    try:
        Machine.neopixel(id).effect(body=params['body'])
    except BaseException as e:
        return make_response(jsonify(str(e)), 401)
    return render_state()


@neopixels_api.route('/neopixel/<id>/rainbow', methods=API_METHODS)
def rainbow(id):
    params = request.get_json()
    Machine.neopixel(id).rainbow(speed=params['speed'])
    return render_state()
