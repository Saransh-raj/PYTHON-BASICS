# A dictionary is an ordered, mutable collection of key-value pairs. Each key must be unique, while values can be duplicated.
student = {
    "name": "Saransh",
    "age": 20,
    "branch": "CSE",
    "cgpa": 8.5
}

print(student)
# accessing the index
print(student["name"])
print("------------------------")

# traversing the key
for key in student:
    print(key)
print("------------------------")

# traverse the values
for value in student.values():
    print(value)
print("------------------------")

# using get()
print(student.get("name"))
print("------------------------")

# updating values
student = {
    "age": 20
}

student["age"] = 21

print(student)
print("------------------------")
