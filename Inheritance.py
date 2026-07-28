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

# Multilevel inheritance :- 

class Factory:
    def __init__(self,material,zips):
        self.material = material
        self.zips = zips
    
class BhopalFactory(Factory):
    def __init__(self, material, zips,color):
        super().__init__(material, zips)
        self.color = color
        
class PuneFactory(BhopalFactory):
    def __init__(self, material, zips, color,pockets):
        super().__init__(material, zips, color)
        self.pockets = pockets
        
        
        
# Multiple inheritance :-

class Father:

    def money(self):
        print("Father's Money")


class Mother:

    def jewellery(self):
        print("Mother's Jewellery")


class Child(Father, Mother):
    pass


c = Child()

c.money()
c.jewellery()