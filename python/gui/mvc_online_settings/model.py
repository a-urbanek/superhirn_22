import sys
sys.path.insert(0, '..')

from config import config

class Model:
    def __init__(self):

        self._super_mode = False
        self.online_mode = False
        self.port = ""
        self.ip_address = ""
        self.update_super_mode()

    @property
    def super_mode(self):
        return self._super_mode

    @super_mode.setter
    def super_mode(self, value):
        self._super_mode = value
        self.update_super_mode()

    def update_super_mode(self):
        config.IS_SUPERHIRN = self._super_mode
        print("update")
