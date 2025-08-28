class Vehicle:
    def move(self):
        pass  # Abstract behavior to be defined in subclasses

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛴️")

# Using polymorphism
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()
