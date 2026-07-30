# Access Modifier :- they are the mechanisms used to control the visibility and accessibility of class members
# There are 3 type of access modifier in python : 1) Public ; 2) Private ; 3) Protected

# 1. Public Access Modifier :- A public Access Modifier can be access from anywhere , it has no underscore before its name
class Student:
    def __init__(self):
        self.name = "Saransh"
        
    def display(self):
         print(self.name)
         
s = Student()
s.display()


# 2. Protected Access Modifier :- A protected member is intended to be used inside the class and its subclasses .It starts with a single underscore (_)

class Student:

    def __init__(self):
        self._name = "Saransh"


s = Student()

print(s._name)

# procted with inheritance
class Parent:
    def __init__(self):
        self._money =  50000
        
class Child(Parent):
    def show(self):
        print(self._money)

c = Child()
c.show()


# 3. Private Access Modifier :- Private members are intended to be accessed only inside the class.They begin with double underscores (__).

class Student:
    def __init__(self):
        self.__age = 20
        
s = Student()
print(s._Student__age) # Syntax for accessing private access modifier variable