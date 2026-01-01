# use while loop to continously ask for name untill the user gives the name

#try 1 using boolean concept:

#name = input("Enter your name: ")
#n1 = bool(name)
#
#while not n1: # while name == "":
#    print("!!! You have to enter your name to further proceed")
#    name = input("Enter your name: ")
#    n1 = bool(name) # won't need this
#
#print(f"Hello {name}")

# use while loop to write a code where user keeps entering his food until 'q' is pressed

food = input("Enter a food name you like: ")

while food != 'q':
    food = input("Enter another food name you like: ")
