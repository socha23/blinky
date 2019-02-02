#!/usr/bin/python3

from flask import Flask, render_template, jsonify
from led_api import led_api
from fire_api import fire_api
from neopixels_api import neopixels_api
from time import time

from machine import Machine


app = Flask(__name__)
app.register_blueprint(led_api)
app.register_blueprint(fire_api)
app.register_blueprint(neopixels_api)


def render_state():
    resp = jsonify(Machine.state())
    resp.status_code = 200
    return resp


@app.route('/')
def index():
    return render_template('index.html', cachebuster=time())


@app.route('/state')
def state():
    return render_state()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
