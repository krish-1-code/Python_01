#This program is for the if-else statements

#wap to decide if one can drive or not


#age = input("Enter your age: ")

#if age > 18:
#    print("Your can drive")
#else:
#    print("No, you can't drive")


# see there was a problem with that code
# when we take input, it's stored as a string data type
# we can't perform comparison operation on string that's why
# we typecasted the string data type to integer
# we'll discuss typecasting in depth in next program. 


age = int(input("Enter your age: "))

if age > 18:
    print("Your can drive")
else:
    print("No, you can't drive")



#Wap to see if someone is online or not.

Is_online = False

if Is_online:
    print("Yes he is online")
else:
    print("No he isn't online")
    