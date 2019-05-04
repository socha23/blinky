from flask import Blueprint, render_template, jsonify
from machine import Machine
from time import time

main_api = Blueprint('main api', __name__)

API_METHODS = ['GET', 'PUT']


def render_success():
    resp = jsonify({'success': True})
    resp.status_code = 200
    return resp


def render_state():
    resp = jsonify(Machine.state())
    resp.status_code = 200
    return resp


@main_api.route('/')
def index():
    return render_template('index.html', cachebuster=time())


@main_api.route('/debug')
def debug():
    return render_template('index.html', cachebuster=time())


@main_api.route('/settings/<id>')
def setttings(id):
    return render_template('index.html', cachebuster=time())


@main_api.route('/state')
def state():
    return render_state()
