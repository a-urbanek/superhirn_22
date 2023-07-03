import sys
sys.path.insert(0, '..')

from config import config, game_config

class Model:
    def __init__(self):

        self._super_mode = False
        self.online_mode = False
        self.port = "5001"
        self.ip_address = "141.45.39.112"
        self.update_super_mode()
        self.update_online_mode()

    @property
    def super_mode(self):
        return self._super_mode

    @super_mode.setter
    def super_mode(self, value):
        self._super_mode = value
        self.update_super_mode()

    def update_super_mode(self):
        config.IS_SUPERSUPERHIRN = self._super_mode
        print("update")

    @property
    def online_mode(self):
        return self._online_mode

    @online_mode.setter
    def online_mode(self, value):
        self._online_mode = value
        self.update_online_mode()

    def update_online_mode(self):
        if self._online_mode:
            game_config.coder_is_computer_server = True
            game_config.coder_is_computer_local = False
            game_config.computer_is_network = True
        else:
            game_config.coder_is_computer_server = False
            game_config.coder_is_computer_local = True
            game_config.computer_is_network = False