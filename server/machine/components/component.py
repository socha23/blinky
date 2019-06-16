class Component:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self._setting = ''
        self._setting_params = {}
        self._on = False

    @property
    def setting(self):
        return self._setting

    @setting.setter
    def setting(self, val):
        self._setting = val

    def on(self, effect=True):
        self._on = True
        self._turn_on(effect)

    @property
    def is_on(self):
        return self._on

    def off(self, effect=True):
        self._on = False
        self._turn_off(effect=effect)

    def update_params(self, params):
        self._setting_params.update(params)
        self._update_current_setting()

    def set_setting_and_params(self, setting, params):
        self.setting = setting
        self._setting_params.update(params)
        self._update_current_setting()

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'on': self._on,
            'setting': self.setting,
            'params': self._setting_params,
            'value': self._current_value(),
            'type': self._type(),
        }

    def _param_generator(self, name):
        while True:
            yield self._setting_params[name] if name in self._setting_params else 0

    def load(self, obj):
        self.set_setting_and_params(obj['setting'], obj['params'])

    def save(self):
        return {'setting': self.setting, 'params': self._setting_params}

    def _current_value(self):
        raise Exception("_current_value not implemented")

    def _turn_on(self, effect=True):
        raise Exception("_turn_on not implemented")

    def _turn_off(self, effect=True):
        raise Exception("_turn_off not implemented")

    def _update_current_setting(self):
        raise Exception("_turn_on_current_setting not implemented")

    def _type(self):
        raise Exception("_type not implemented")
