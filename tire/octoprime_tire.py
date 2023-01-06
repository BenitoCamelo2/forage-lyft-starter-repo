from .tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, front_right, front_left, rear_right, rear_left):
        self.front_right = front_right
        self.front_left = front_left
        self.rear_right = rear_right
        self.rear_left = rear_left

    def needs_service(self):
        return self.front_right + self.front_left + self.rear_right + self.rear_left > 3.0