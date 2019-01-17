#!/usr/bin/python

from flask import Flask
from flask import render_template
from gpiozero import PWMLED

app = Flask(__name__)

PINS_WITH_LEDS = [24, 25]

leds = {pin: PWMLED(pin) for pin in PINS_WITH_LEDS}


@app.route('/')
def index():
    return render_template('index.html')


def led(pin):
    return leds[int(pin)]


@app.route('/<pin>/on')
def on(pin):
    led(pin).on()
    return render_template('index.html', leds=PINS_WITH_LEDS)


@app.route('/<pin>/off')
def off(pin):
    led(pin).off()
    return render_template('index.html', leds=PINS_WITH_LEDS)


@app.route('/<pin>/blink')
def blink(pin):
    led(pin).blink()
    return render_template('index.html', leds=PINS_WITH_LEDS)


@app.route('/<pin>/pulse')
def pulse(pin):
    led(pin).pulse()
    return render_template('index.html', leds=PINS_WITH_LEDS)


@app.route('/<pin>/pwm/<val>')
def pwm(pin, val):
    led(pin).value = float(val)
    return render_template('index.html', leds=PINS_WITH_LEDS)


if __name__ == "__main__":
    led(24).on()
    app.run(host='0.0.0.0', port=80)
