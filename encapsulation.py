# Encapsulation :- Wrapping data (variables) and methods (functions) into a single unit called a class and controlling access to the data.

# basic encapsulation code :-
class Student:
    def __init__(self):
        self.name = "Saransh"
        
    def display(self):
        print(self.name)
        
s = Student()
s.display()

# Getter method :- A getter method allow safe reading of private data
class Student:
    
    def __init__(self):
        self.__age = 20

    def get_age(self):
        return self.__age
    
s = Student()
print(s.get_age())

# Setter method :- A setter allow control updates
class Student:

    def __init__(self):
        self.__age = 20
        
    def set_age(self,age):
        if age > 0:
            self.__age = age
            
    def get_age(self):
            return self.__age       
    
s = Student()
s.set_age(25)
print(s.get_age())