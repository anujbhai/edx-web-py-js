class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point_1 = Point(105.4, 80.09)

print(f"point 1: {point_1.x}")
print(f"point 2: {point_1.y}")


class Flight:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self, name):
        if not self.seats_available():
            return False
        self.passenger.append(name)
        return True

    def seats_available(self):
        return self.capacity - len(self.passenger)


flight = Flight(3)

people = ["Ravi", "Chandrakala", "Tanu", "Rolex"]

for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No seats available for {person}")
