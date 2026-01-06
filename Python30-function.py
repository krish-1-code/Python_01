#function = block of code that we can all intead of writing that code again and again

#to make a function use def as for define

def happybday(name):
    print(f"Happy birthday {name}")

#happybday("Krish")


#making a small calculator:

def sum(num1 , num2):
    return num1 + num2

def substract(num1 , num2):
    return  num1 - num2

def multiply(num1 , num2):
    product = num1 * num2
    return product

def divide(num1 , num2):
    div = num1 / num2
    return div

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The sum is {sum(num1,num2)}")
print(f"The difference is {substract(num1,num2)}")
print(f"The product is {multiply(num1,num2)}")
print(f"The divide is {divide(num1,num2):.05f}")



