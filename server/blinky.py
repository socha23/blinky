#!/usr/bin/python3

from flask import Flask
from api.component_api import component_api
from api.main_api import main_api
from filestore import Filestore
from machine.machine import Machine
from my_machine import setup

setup(Machine)

Machine.initialize(Filestore("/tmp/blinky.json"))

app = Flask(__name__)
app.register_blueprint(main_api)
app.register_blueprint(component_api)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
