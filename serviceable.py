from abc import ABC, abstractmethod
from car import Car

class Serviceable(Car, ABC):
    def __init__(self, Car):
        super().__init__(Car)
        self.Car = Car
    
    @abstractmethod
    def needs_service():
        pass