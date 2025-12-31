#unlike c where we had to specificly mention about the variable
#python automatically detects the variable type based on the value assigned to it
#variablres are case sensitive in python
#common variable types in python are: int, float, string and boolean
# to assign a value to a variable we use assignmnet operator '='

#WAP to create a variable of each type and print their values and types

name = "Krish" # this is a string variable
age = 21      # this is an integer variable
height = 5.9  # this is a float variable
is_student = True # this is a boolean variable. This can only be true or false

print(f"Name: {name}. This is a {type(name)} variable")
print(f"Age: {age}. This is a {type(age)} variable")
print(f"{is_student}")


# the f is called f-string or format-string which allows us to display the variable 
# along with the text we want to print.