from .tire import Tire

class CarriganTire(Tire):
    def __init__(self, front_right, front_left, rear_right, rear_left):
        self.front_right = front_right
        self.front_left = front_left
        self.rear_right = rear_right
        self.rear_left = rear_left

    def needs_service(self):
        return self.front_right > 0.9 or self.front_left > 0.9 or self.rear_right > 0.9 or self.rear_left > 0.9