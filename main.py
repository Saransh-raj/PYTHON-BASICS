print("Hello....!")
print("Saransh \nRaj")

name = "Saransh"
age = 20
PI = 3.14

# printing the type of variable
print(type(name)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(PI)) # <class 'float'>

# sum of two numbers
a = 10
b = 15
c = a+b
print(c)

# type conversion
# String to Integer
s = "100"
a = int(s)
print(a, type(a))   # 100 <class 'int'>

# Number to String
num = 42
label = str(num)
print(label, type(label))   # "42" <class 'str'>

# variable naming
studentName = "Saransh" # camel case

StudentName = "Saransh" # pascal case

student_name = "Saransh" # snake case

# for know the unicode of anything
a = "A"
print(ord(a))

# index accessing
str = "HELLO"
#         H              E              L
print(str[0]); print(str[1]); print(str[2])

# string slicing
let = "SHER CODER"
print(let[0:4]) # SHER
print(let[5:]) # CODER
