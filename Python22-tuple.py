#tuples are exactly like list 
#only differnce being it's unchangeable and faster.

fruits = ["Apple","Banana","Mango"]

print(fruits[-1::-1])

print(fruits[-1])

fruits.pop()
fruits.pop()

print(fruits)

#using some string methods

print("Orange" in fruits) 

#adding an item at the last index:

fruits.append("Guava")
print(fruits)

#to add an item at a specific index:

fruits.insert(0,"Mango")
print(fruits)

# To find index of an item:

print(fruits.index("Guava"))

#To find the occurence ofan item:

print(fruits.count("Apple"))

#To find number of items in the list

print(len(fruits))

# To sort a list

fruits.sort()
print(fruits)

#To reverse a list

fruits.reverse()
print(fruits)

#To clear a list:

fruits.clear()
print(fruits)
