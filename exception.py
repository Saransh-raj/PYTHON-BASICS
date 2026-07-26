# An exception is an error that occurs during the execution (runtime) of a program.
# When Python encounters an exception, it stops the program unless the exception is handled.

try:
    a = 10
    b = 0
    print(a / b)

except:
    print("Cannot divide by zero")
    
# Handling Specific Exceptions
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Division by zero is not allowed")
    
# Multiple Exceptions
try:
    num = int(input("Enter number: "))
    print(10 / num)

except ValueError:
    print("Invalid Input")

except ZeroDivisionError:
    print("Cannot divide by zero")
    
# Using Exception as a Variable
try :
    print(10/0)
except Exception as e:
    print(e)
    
# try-except-else
# The else block executes only if no exception occurs.
try:
    a = 10
    b = int(input("Enter number : "))
    print(a/b)
except ZeroDivisionError:
    print("Division by zero not possible...!")
else:
    print("Division Successfull..!")
    
# try-except-finally
# The finally block always executes whether an exception occurs or not.
try:
    print(10 / 2)

except:
    print("Error")

finally:
    print("Program Finished")
    
# Raising Exceptions
# You can create your own exception using raise.

# age = -5
# if age < 0:
#     raise ValueError("Age cannot be negative")


# user define exception
# class InvalidAgeError(Exception):
#     pass

# age = -2

# if age < 0:
#     raise InvalidAgeError("Invalid Age")