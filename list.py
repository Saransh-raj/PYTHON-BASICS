# A list is a collection of multiple values stored in a single variable.

numbers = [10, 20, 30, 40]
fruits = ["Apple", "Banana", "Mango"]
mixed = [10, "Python", 3.14, True]

# In list index start form 0 
print(numbers[0])

# traversibg in list using for loop
for i in range(len(fruits)):
    print(fruits[i])
    
# one more way to traverse 
for fruit in fruits:
    print(fruit)
    
# changing an element in list 
# list are mutable we can change the element

nums = [10, 20, 30]

nums[1] = 100

print(nums)

# we can also do the slicing in list
print(fruits[0:2])

# To know the method of the list 
print(dir(list))

# insert the element into list
l = [1,3,4,5]
l.insert(1,2)
print(l)

# add the element to the end
fruits.append("Cherry")
print(fruits)

# add multiple element to the end
numbers.extend([70,80,90])
print(numbers)

# remove method - it remove the first occurence of any element
numbers.remove(10)
print(numbers)

# pop the element from the list
pop_item = numbers.pop(2) # pass index value
print(numbers)

# count method in list, it count the occurences of element
count = numbers.count(90)
print(count)

# sort the list into ascending order
numbers.sort()
print(numbers)

# reverse method 
numbers.reverse()
print(numbers)

# create the copy of the list 
new_num = numbers.copy()
print(new_num)

# print the negative and posotive element of the list
l2 = [-11,-7,8,5,9,-4,-3,4,-8]
# print positive element
print("Positive elements are : ")
for i in l2:
    if i >= 0:
        print(i)

# print negative element
print("Negative element are : ")
for i in l2:
    if i < 0:
        print(i)
        
# mean of the list element
l3 = [12.14,16,18,20]
sum = 0
for i in l3:
    sum = sum + i

mean = sum/len(l3)

print("Mean : ",mean)

# find the maximum into list 
l4 = [10,9,3,4,11,15,42]
max = l4[0]
for i in l4:
    if i > max:
        max = i
print(max)

# second largest element into list
l4 = [10,9,3,4,11,15,42]
max = l4[0]
sec_max = l4[0]
for i in l4:    
    if i > max:
        sec_max = max
        max = i
    elif i>sec_max:
        sec_max = i
print("Second max - ",sec_max)    

# find the minimum into list 
l4 = [10,9,3,4,11,15,42]
min = l4[0]
for i in l4:
    if i < min:
        min = i
print(min)

# check if list is sorted or not
l5 = [10,3,5,50,41,9,2,45]
for i in range(len(l5)):
    if l5[i] > l[i+1]:
        print("Not sorted")
        break
    else:
        print("Sorted")