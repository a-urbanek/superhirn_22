from abc import ABC, abstractmethod

class Command(ABC):
    """
    This is an abstract method that needs to be implemented by a subclass and takes a main_app
    parameter.
    
    :param main_app: The main application object that the method will interact with or modify.
    """
    @abstractmethod
    def execute(self, main_app):
        pass

    """
    This is an abstract method that defines a string representation of an object.
    """
    @abstractmethod
    def __str__(self):
        pass