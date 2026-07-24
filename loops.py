# A loop is a programming concept that allows you to execute the same block of code multiple times without writing it repeatedly

for i in range(5):
    print("Hello")
print("------------------------")

    
for i in range(5):
    print(i)
print("------------------------")
    
# range(start, stop)
for i in range(2,6):
    print(i)
print("------------------------")

# range(start, stop, step)
# The third value is called the step size.
for i in range(1,11,2):
    print(i)
print("------------------------")

# reverse number printing
for i in range(10,0,-1):
    print(i)
print("------------------------")

# printing table :
num = int(input("Enter number : "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}",)
    
# one more method for printing the table
#for i in range(n,(n*10)+1,n): 
#    print(i)
print("------------------------")


name = "Python"

for ch in name:
    print(ch)
print("------------------------")
      
      
# while
i = 1
while i <= 5:
    print(i)
    i += 1

# Print odd numbers from 1 to 50.
for i in range(51):
    if i % 2 != 0:
        print(i)
print("------------------------")

# Find the sum of numbers from 1 to n.
sum = 0
num1 = int(input("Enter numer till where you want to find the sum : "))
for i in range(1,num1+1):
    sum+=i
print(sum)
print("------------------------")

# directly accessing the loop without range function
str = "STRANGER THINGS"
for i in str:
    print(i)
print("------------------------")

# break keyword :- The break statement is used to immediately terminate (stop) a loop.
for i in range(1,10):
    if i == 6:
        break
    else:
        print(i)
print("------------------------")

        
# break keyword question :- 
correct_password = "Saransh@123"

while True:
    password = input("Enter password : ")
    
    if correct_password == password:
        print("User login successfully..!")
        break
    
    print("Wrong password --- :(")
print("------------------------")



# continue keyword :- The continue statement is used to skip the current iteration of a loop and continue with the next iteration
for i  in range(1,10):
    if i == 8:
        continue
    else:
        print(i)
print("------------------------")

# Print Only Odd Numbers using continue statement
for i in range(1,15):
    if i % 2 == 0:
        continue
    print(i)

