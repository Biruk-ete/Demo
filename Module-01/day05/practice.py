from abc import ABC, abstractmethod

class Vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def describe(self):
        return f"Make: {self.make}, Model: {self.model}"

    @abstractmethod
    def wheels(self):
        pass

class Car(Vehicle):
    def wheels(self):
        return 4

class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity
    
    def describe(self):
        return f"{super().describe()}, Capacity: {self.capacity}"

    def wheels(self):
        return 18

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
truck1 = Truck("Volvo", "FSR", "50 tons")

vehicles = [car1, car2, truck1]

for vehicle in vehicles:
    print(vehicle.describe())
    print("Wheels:", vehicle.wheels())