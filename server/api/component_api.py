from flask import Blueprint, request, jsonify, make_response
from api.main_api import render_state
from machine_service import component_off, component_on, set_component_setting, update_component_params

component_api = Blueprint('component api', __name__)

API_METHODS = ['GET', 'PUT']


@component_api.route('/component/<component_id>/on', methods=API_METHODS)
def on(component_id):
    component_on(component_id)
    return render_state()


@component_api.route('/component/<component_id>/off', methods=API_METHODS)
def off(component_id):
    component_off(component_id)
    return render_state()


@component_api.route('/component/<component_id>/params', methods=API_METHODS)
def do_update_component_params(component_id):
    try:
        update_component_params(component_id, request.get_json())
    except BaseException as e:
        return make_response(jsonify(str(e)), 400)
    return render_state()


@component_api.route('/component/<component_id>/setting/<setting_name>', methods=API_METHODS)
def do_set_component_setting(component_id, setting_name):
    try:
        set_component_setting(component_id, setting_name, request.get_json())
    except BaseException as e:
        return make_response(jsonify(str(e)), 400)
    return render_state()
