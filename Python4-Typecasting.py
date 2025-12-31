#Typecasting is the process of changing the data type of a variable.

#Why is typecasting important?

#The inputs we take from the user are in string datatype and we can't perform opertaions on string
#So it necessasry that we chnage the datatype 

#following are the examples of each of the typecasting.

name = "Krish"

name = int(name)
print(type(name))

#this gives error cuz int are supposed to be numbers and not characters

#another example:

age = int(input("Enter the number: "))

print(type(age))
