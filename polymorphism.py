# Polymorphism is the ability of the same method, function, or operator to behave differently depending on the object or data it is working with.

class Animal:

    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Duck typing in python :-

# Example 1 :-

class Bike:

    def start(self):
        print("Bike Started")


class Car:

    def start(self):
        print("Car Started")


class Bus:

    def start(self):
        print("Bus Started")

# duck typing function
def vehicle_start(vehicle):
    vehicle.start()


vehicle_start(Bike())
vehicle_start(Car())
vehicle_start(Bus())


# Example 2 :-

class Car:

    def sound(self):
        print("Horn")


class Dog:

    def sound(self):
        print("Bark")

# duck typing function
def play(obj):
    obj.sound()


play(Car())
play(Dog())