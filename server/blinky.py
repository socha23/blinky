#!/usr/bin/python

from flask import Flask, render_template, jsonify
from time import time

from my_machine import MyMachine

app = Flask(__name__)

machine = MyMachine()


API_METHODS = ['GET', 'PUT']


def render_state():
    resp = jsonify(machine.state())
    resp.status_code = 200
    return resp


@app.route('/')
def index():
    return render_template('index.html', leds=[24, 25], cachebuster=time())


@app.route('/state')
def state():
    return render_state()


@app.route('/led/<pin>/on', methods=API_METHODS)
def on(pin):
    machine.led(pin).on()
    return render_state()


@app.route('/led/<pin>/off', methods=API_METHODS)
def off(pin):
    machine.led(pin).off()
    return render_state()


@app.route('/led/<pin>/blink', methods=API_METHODS)
def blink(pin):
    machine.led(pin).blink()
    return render_state()


@app.route('/led/<pin>/pulse', methods=API_METHODS)
def pulse(pin):
    machine.led(pin).pulse()
    return render_state()


@app.route('/led/<pin>/pwm/<val>', methods=API_METHODS)
def pwm(pin, val):
    machine.led(pin).pwm(val)
    return render_state()

if __name__ == "__main__":
    machine.led(24).on()
    app.run(host='0.0.0.0', port=80)