# tuple - The elements have a defined sequence, and you can access them by index (just like lists).
#         immutable Once created, you cannot change, add, or remove elements in a tuple.

# syntax :-
# Creating a tuple
my_tuple = (10, "hello", 3.14,10)

# Accessing elements
print(my_tuple[0])   # Output: 10
print(my_tuple[1])   # Output: hello

# Tuples can also be nested
nested_tuple = (1, (2, 3), 4)
print(nested_tuple[1])  # Output: (2, 3)

# methods :- there are only two methods in tuple
index = my_tuple.index(10) # find the index of first occurrence of 10
count = my_tuple.count(10) # count occurrence of 10

print(index)
print(count)

# Tuple unpacking :- 
a,b,c,d = (1,2,3,4)
print(a)    # 1
print(b)    # 2