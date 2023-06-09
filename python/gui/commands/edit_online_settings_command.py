from .command import Command


# The EditOnlineSettings class 
class EditOnlineSettings(Command):
    def execute(self, main_app):
        print("Online Settings")

    def __str__(self):
        return "Online Settings"