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

    def on(self):
        self._turn_on_current_setting()

    def off(self):
        self._on = False
        self._turn_off()

    def update_params(self, params):
        self._setting_params.update(params)
        self._on = True
        self._turn_on_current_setting()

    def set_setting_and_params(self, setting, params):
        self.setting = setting
        self._setting_params.update(params)
        self._on = True
        self._turn_on_current_setting()

    def state(self):
        return {
            'id': self.id,
            'name': self.name,
            'on': self._on,
            'setting': self.setting,
            'params': self._setting_params
        }

    def _param_generator(self, name):
        while True:
            yield self._setting_params[name] if name in self._setting_params else 0

    def _turn_off(self):
        raise Exception("_turn_off not implemented")

    def _turn_on_current_setting(self):
        raise Exception("_turn_on_current_setting not implemented")

