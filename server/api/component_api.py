from flask import Blueprint
from api.main_api import render_state
from machine_service import component_off, component_on

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
