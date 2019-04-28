from flask import Blueprint
from api.main_api import render_success
from machine_service import fire_on, fire_off, fire_set_intensity

fire_api = Blueprint('fire api', __name__)

API_METHODS = ['GET', 'PUT']


@fire_api.route('/fire/<fire_id>/on', methods=API_METHODS)
def on(fire_id):
    fire_on(fire_id)
    return render_success()


@fire_api.route('/fire/<fire_id>/intensity/<intensity>', methods=API_METHODS)
def set_intensity(fire_id, intensity):
    fire_set_intensity(fire_id, float(intensity))
    return render_success()


@fire_api.route('/fire/<fire_id>/off', methods=API_METHODS)
def off(fire_id):
    fire_off(fire_id)
    return render_success()
