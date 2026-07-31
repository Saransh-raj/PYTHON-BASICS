# decorator is a function that takes another function as a input, add some extra functionality to it and returns the modified function without changing its original value

# Without decorator :-
class Animal:
    def show(self):
        print("Animal")
obj = Animal()
obj.show() # after show there is a parenthesis in without decorator example

# with decorator
class Animal:
    @property
    def show(self):
        print("Hello Animal")
obj = Animal()
obj.show    # no need of parenthesis after the show using the decorator property

# creating decorator :- for creating a decorator you first have to create a decorator function and insode that we will create a wrapper

def decorator(func): # you can take any name here func is taken
    def wrapper():
        print("I will print myself before the decorator function hello")
        func()
        print("I will print after the function")
    return wrapper
    
@decorator
def hello():
        print("Hello i am saransh raj")
        
hello()

# one more example
def add_decorator(fnc):
    def wrapper(a,b):
        print("The addition to your number : ")
        fnc(a,b)
        print("Thank you")
    return wrapper

@add_decorator
def addition(a,b):
    print(f"The addition is : {a+b}")
    
addition(10,34)