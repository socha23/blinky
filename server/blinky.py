#!/usr/bin/python

from flask import Flask
from flask import render_template
from time import time

from machine import Machine

app = Flask(__name__)

machine = Machine()

machine \
    .add_led(24, "Czerwony") \
    .add_led(25, "Bialy")


API_METHODS = ['GET', 'PUT']


def standard_template():
    return render_template('index.html', leds=[24, 25], cachebuster=time())


@app.route('/')
def index():
    return standard_template()


@app.route('/led/<pin>/on', methods=API_METHODS)
def on(pin):
    machine.led(pin).on()
    return standard_template()


@app.route('/led/<pin>/off', methods=API_METHODS)
def off(pin):
    machine.led(pin).off()
    return standard_template()


@app.route('/led/<pin>/blink', methods=API_METHODS)
def blink(pin):
    machine.led(pin).blink()
    return standard_template()


@app.route('/led/<pin>/pulse', methods=API_METHODS)
def pulse(pin):
    machine.led(pin).pulse()
    return standard_template()


@app.route('/led/<pin>/pwm/<val>', methods=API_METHODS)
def pwm(pin, val):
    machine.led(pin).pwm(val)
    return standard_template()


if __name__ == "__main__":
    machine.led(24).on()
    app.run(host='0.0.0.0', port=80)