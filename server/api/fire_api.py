from flask import Blueprint, jsonify
from my_machine import Machine

fire_api = Blueprint('fire api', __name__)

API_METHODS = ['GET', 'PUT']


def render_success():
    resp = jsonify({'success': True})
    resp.status_code = 200
    return resp


@fire_api.route('/fire/<fire_id>/on', methods=API_METHODS)
def on(fire_id):
    Machine.fire(fire_id).on()
    return render_success()


@fire_api.route('/fire/<fire_id>/intensity/<intensity>', methods=API_METHODS)
def set_intensity(fire_id, intensity):
    Machine.fire(fire_id).intensity = float(intensity)
    return render_success()


@fire_api.route('/fire/<id>/off', methods=API_METHODS)
def off(id):
    Machine.fire(id).off()
    return render_success()
