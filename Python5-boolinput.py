#Is_student = bool(input("Are you a student?: "))

#print(Is_student)


# Bool is an interesting datatype 
# when used for taking input - if values is empty string , it is considered as False
# if there is any value other than empty string, it is considered as True

#it can be used to check if user has entered any value or not 

# WAP where user MUST enter the name otherwise the loop continues

name = bool(input("Enter your name: "))

if name:
    print("Thank you for entering your name")
else:
    while not name:
        name = input("Invalid! Enter your name: ")

