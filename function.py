# function
def greet():
    print("Hello Saransh")

greet()

# function without parameter 
def welcome():
    print("Welcome to python")
    
welcome()

# Arguments :- Arguments are the Values passed to a function when it is called
# function with parameter 
def greeting(name):
    print("Hello ,",name)

greeting("Saransh")

# sum function with parameter 
def sum(a,b):
    print(f"The sum of your number is {a+b}")
    
sum(2,5)
sum(12,10)

# default argument function
def sum2(x,y=42):
    print(f"The sum of your number is {x+y}")

sum2(10)

# function for checking the string is palindrome or not
def palindrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]
        
    if rev == str:
        print("Palindrome")
            
    else:
        print("Not a palindrome")
            
palindrome("Saransh")
palindrome("KANAK")