# Set is unordered and unchangeable; No duplicates
# You can only add and remove item from here

fruits = {"Apple","Banana","Orange"}

print(fruits) # it's unordered if you use index you will run into an error

fruits.add("Coconut")

print(fruits)

fruits.remove("Apple")

print(fruits)

#We can also use pop function; it removes the last index; but 
# since set doesn't work on index; it can remove any random item

fruits.pop()
print(fruits)