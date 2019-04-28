#!/usr/bin/python3

from flask import Flask

from api.component_api import component_api
from api.main_api import main_api
from api.led_api import led_api
from api.fire_api import fire_api
from api.neopixels_api import neopixels_api

app = Flask(__name__)
app.register_blueprint(main_api)
app.register_blueprint(component_api)
app.register_blueprint(led_api)
app.register_blueprint(fire_api)
app.register_blueprint(neopixels_api)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
