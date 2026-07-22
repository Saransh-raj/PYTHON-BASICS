# if else statement in python
age = int(input("Enter age : "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible")
    
# code for checking Even or Odd
num = int(input("Enter number for checking Even or Odd : "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
    

# if elif else statement : 
marks = int(input("Enter marks : "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    

# Nested if statement : 
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Not eligible")
    
# print the largest og 2 numbers 
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))
if a>b:
    print(a," is greater")
else:
    print(b," is greater")
    
# Login check :
password = input("Enter the pasword : ")
if password == "saransh@123":
    print("Login Successful..!")
else:
    print("Incorrect Password..!")
    
# greatest of the three numbers 
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
num3 = int(input("Enter number 3 : "))
if num1 >  num2 and num1 > num3:
    print(num1," is greater")
elif num2 > num1 and num2 > num3:
    print(num2, "is greater")
else:
    print(num3," is greater")