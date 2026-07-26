# File handling allows a Python program to create, read, write, update, and delete files stored on your computer.

p = open(r'C:\Users\cools\OneDrive\Desktop\PYTHON BASIC\file.txt')
print(p.read())

# multiple modes to open a file
# 1. 'r' mode - read the file
# 2. 'w' mode - use to create file
# 3. 'a' mode - use to append (add to end of file)
# 4. 'x mode - use to create a new file (fail if it is exist)

# create one file which name is superman.txt
s = open("Superman.txt",'w') # 'w' is used to write something into file

# now write something into the file which you created
s.write("Hello this is saransh raj from Bihar ")
s.close()

# append something into the superman.txt file
s = open("Superman.txt",'a') # 'a' is used to append something into file

s.write("\nCurrently doing my B.tech from Parul University")
s.close()

# to read the file 'r' is used
s = open(r"Superman.txt")
print(s.read())