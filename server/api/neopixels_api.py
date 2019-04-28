from flask import Blueprint, jsonify, request, make_response
from api.main_api import render_state
from machine_service import neopixel_setting, neopixel_update_params

neopixels_api = Blueprint('neopixel api', __name__)

API_METHODS = ['GET', 'PUT']


@neopixels_api.route('/neopixel/<id>/params', methods=API_METHODS)
def brightness(id):
    try:
        neopixel_update_params(id, request.get_json())
    except BaseException as e:
        return make_response(jsonify(str(e)), 400)
    return render_state()


@neopixels_api.route('/neopixel/<neopixel_id>/setting/<setting_name>', methods=API_METHODS)
def setting(neopixel_id, setting_name):
    try:
        neopixel_setting(neopixel_id, setting_name, request.get_json())
    except BaseException as e:
        return make_response(jsonify(str(e)), 400)
    return render_state()