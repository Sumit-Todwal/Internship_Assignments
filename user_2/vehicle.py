from abc import ABC, abstractmethod

# Abstraction using Abstract Base Class
class Vehicle(ABC):
    def __init__(self, brand, model):
        self._brand = brand          # Encapsulated attribute
        self._model = model          # Encapsulated attribute

    def get_info(self):
        return f"{self._brand} {self._model}"

    @abstractmethod
    def start_engine(self):         # Abstract method (force subclasses to implement)
        pass

# Inheritance
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self._seats = seats

    # Polymorphism - different behavior for same method name
    def start_engine(self):
        return f"{self.get_info()} engine started with a key."

    def get_seats(self):
        return self._seats

class Bike(Vehicle):
    def __init__(self, brand, model, cc):
        super().__init__(brand, model)
        self._cc = cc

    def start_engine(self):
        return f"{self.get_info()} engine started with a self-kick."

    def get_cc(self):
        return self._cc

# Object creation
vehicles = [
    Car("Toyota", "Camry", 5),
    Bike("Yamaha", "R15", 155)
]

# Using polymorphism and encapsulation
for v in vehicles:
    print(v.start_engine())
