#WAP that validates yout usernmae
#username has to
#  1. no more than 12 char
# 2. no spaces
# 3. no digits

user_name = input("Ente your user name:")

length = len(user_name)

if length>12:
    print("Username can't me more than 12 characters")

elif user_name.count(" ") > 0:
    print("Username can't have any spaces")

elif not user_name.isalpha():
    print("Username can't have spaces or special characters")

else:
    print(f"Greetings {user_name}")