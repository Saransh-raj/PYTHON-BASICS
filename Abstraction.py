# Abstraction :-  Abstraction is a process of hiding implementation details and showing only essential details to user

# below code is abstract method
from abc import ABC, abstractmethod
# abstract class
class Animal(ABC):
    @abstractmethod
    def Sound(self):
        pass

# child class
class Dog(Animal):
    def Sound(self):
        print("Bark")
        
d = Dog()
d.Sound()


# multiple abstract method  :---

# abstract class
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

# child class
class Car(Vehicle):
    def start(self):
        print("Car Started")
        
    def stop(self):
        print("Car Stopped")
        
c = Car()
c.start()
c.stop()