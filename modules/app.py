from abc import ABC, abstractmethod, abstractproperty


class App(ABC):
    app_name = "App Name"
    @abstractmethod
    def start():
        pass
