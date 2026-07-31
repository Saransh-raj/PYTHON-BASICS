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


# Real world example (payment system) :-

# abstract class
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

# child class
class CreditCard(Payment):

    def pay(self):
        print("Payment through Credit Card")

# child class
class UPI(Payment):

    def pay(self):
        print("Payment through UPI")
        
p1 = CreditCard()
p2 = UPI()

p1.pay()
p2.pay()