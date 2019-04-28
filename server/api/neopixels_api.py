from flask import Blueprint, jsonify, request, make_response
from api.main_api import render_state
from machine_service import neopixel_brightness, neopixel_effect, neopixel_fire, neopixel_off, neopixel_on, neopixel_rainbow, neopixel_rgb

neopixels_api = Blueprint('neopixel api', __name__)

API_METHODS = ['GET', 'PUT']


@neopixels_api.route('/neopixel/<id>/on', methods=API_METHODS)
def on(id):
    neopixel_on(id)
    return render_state()


@neopixels_api.route('/neopixel/<id>/off', methods=API_METHODS)
def off(id):
    neopixel_off(id)
    return render_state()


@neopixels_api.route('/neopixel/<id>/brightness/<brightness>', methods=API_METHODS)
def brightness(id, brightness):
    neopixel_brightness(id, float(brightness))
    return render_state()


@neopixels_api.route('/neopixel/<id>/fire', methods=API_METHODS)
def fire(id):
    neopixel_fire(id)
    return render_state()


@neopixels_api.route('/neopixel/<id>/rgb', methods=API_METHODS)
def rgb(id):
    neopixel_rgb(id, request.get_json())
    return render_state()


@neopixels_api.route('/neopixel/<id>/effect', methods=API_METHODS)
def effect(id):
    try:
        neopixel_effect(id, request.get_json())
    except BaseException as e:
        return make_response(jsonify(str(e)), 401)
    return render_state()


@neopixels_api.route('/neopixel/<id>/rainbow', methods=API_METHODS)
def rainbow(id):
    neopixel_rainbow(id, request.get_json())
    return render_state()
