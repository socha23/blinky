#!/usr/bin/python

from flask import Flask
from flask import render_template
from gpiozero import LED, PWMLED

app = Flask(__name__)



led = PWMLED(25)

@app.route('/')
def index():
  return render_template('index.html')  

@app.route('/on')
def on():
  led.on()
  return render_template('index.html')


@app.route('/off')
def off():
  led.off()
  return render_template('index.html')

@app.route('/blink')
def blink():
  led.blink()
  return render_template('index.html')

@app.route('/pulse')
def pulse():
  led.pulse()
  return render_template('index.html')

@app.route('/pwm/<val>')
def pwm(val):
  led.value=float(val)
  return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
