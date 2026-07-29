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

