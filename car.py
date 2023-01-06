from abc import ABC, abstractmethod
from engine.engine import Engine
from battery.battery import Battery

class Car(Engine, Battery, ABC):
    def __init__(self, Engine, Battery):
        super().__init__(Engine, Battery)
        self.Engine = Engine
        self.Battery = Battery

    @abstractmethod
    def needs_service(self):
        pass
