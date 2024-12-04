import random

class Elevator:
    def __init__(self, total_floors, capacity):
        self.total_floors = total_floors
        self.capacity = capacity
        self.current_floor = 1
        self.direction = 1
        self.passengers = []

    def simulate_turn(self):
        self.passengers = [x for x in self.passengers if x != self.current_floor]

        available_space = self.capacity - len(self.passengers)
        new_passenger_count = min(available_space, random.randint(1, 5))

        for _ in range(new_passenger_count):
            target_floor = random.randint(1, self.total_floors)
            if target_floor != self.current_floor:
                self.passengers.append(target_floor)

        self.current_floor += self.direction
        if self.current_floor in {self.total_floors, 1}:
            self.direction *= -1

    def status(self):
        direction_str = "up" if self.direction == 1 else "down"
        return (
            f"Elevator is on floor {self.current_floor}, moving {direction_str}.\n"
            f"Passengers: {self.passengers}"
        )