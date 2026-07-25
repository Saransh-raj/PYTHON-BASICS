# A set is an unordered collection of unique elements. Think of it like a mathematical set: no duplicates, and the order doesn’t matter.
# it is muttable
my_set = {1, 2, 3, 4, 4, 2}
print(my_set) 

# Add an element
my_set.add(5)

# Remove an element
my_set.remove(2)

# Check membership
print(3 in my_set)   # True

# Set operations
A = {1, 2, 3}
B = {3, 4, 5}

print(A.union(B))        # {1, 2, 3, 4, 5}
print(A.intersection(B)) # {3}
print(A.difference(B))   # {1, 2}


# adding multiple elements in set
numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)

# pop element from set
removed = numbers.pop()

print(removed) # store the removed value 
print(numbers)

# set operations
# 1. union
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)

# 2. Intersection
A = {1, 2, 3}
B = {2, 3, 4}

print(A & B)

# 3. Difference
A = {1, 2, 3}
B = {2, 3, 4}

print(A - B)

