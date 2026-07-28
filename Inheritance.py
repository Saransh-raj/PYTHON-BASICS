class Factory_Mumbai():
    a = "I am an attribute mention inside a factory"
    def hello(self):
        print("Hello i am method mentioned inside a factory")
        
# Factory_Pune inherit property from Factory_Mumbai
class Factory_Pune(Factory_Mumbai):
    pass

obj = Factory_Mumbai
print(obj.a)

obj2 = Factory_Pune
print(obj2.a)

# super keyword :- 
class Animal:
    def __init__(self):
        print("Animal Constructor")
        
class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog Constructor")
        
d = Dog()

