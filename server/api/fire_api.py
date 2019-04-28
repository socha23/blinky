from flask import Blueprint
from api.main_api import render_state
from machine_service import fire_set_intensity

fire_api = Blueprint('fire api', __name__)

API_METHODS = ['GET', 'PUT']


@fire_api.route('/fire/<fire_id>/intensity/<intensity>', methods=API_METHODS)
def set_intensity(fire_id, intensity):
    fire_set_intensity(fire_id, float(intensity))
    return render_state()
