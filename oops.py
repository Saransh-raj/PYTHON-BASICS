# Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects.
# An object contains data (attributes) and functions (methods) that operate on that data.

class Car:
    wheels = 4 # attributes
    
    def running(self): # method
        print("Car is running")

print(Car.wheels) # accessing attributes
Car().running() # calling method

# object - real world entity or instance of a class
# creating object
obj = Car()

print(obj.wheels)
print(obj.running())

# constructor - A constructor is a special method that is called automatically when an object is created.
class Student:
    
    # dunder method
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def show(self):
        print(f"Your student details : Name {self.name} , Roll {self.roll}")

# s1 object 
s1 = Student("Saransh",90)
s1.show()

# s2 student
s2 = Student("Aman",21)
s2.show()

# types of attributes :- 

# 1. class attributes - A normal variable created inside a class is a class attribute and thats it
class Animal:
    name = "Lion" # class attribute
    
# 2. instances attribute - a attribute created using an instance like self.name , self.age etc 
class Animal:
    name = "Lion"
    
    def __init__(self,age):
        self.age = age # instance attribute

# types of method

# 1. Instance method - An instance method Works with instance (object) of the class. This method can access and modify instance attributes.
class Animal:
    def show(self):
        print("Hello how are you...!")
        
# 2. Class method - This method works with the class itself it will not target the instance (object). we have to use 
# @classmethod decorator for creating the class method and it takes cls as their first parameter.0
class Myclass:
    @classmethod
    def class_method(cls):
        print("This is the class")