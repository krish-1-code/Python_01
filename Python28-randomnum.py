import random

#to get a random number between 0 and 1

number = random.random()
print(number)

# to get a integer between a fix set

number = random.randint(1,6)
print(number)

# to get a string

fruits = ("Apple","Banana","XINGXANG")
fruit = random.choice(fruits)
print(fruit)

# to shuffle a list / tupple

cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
random.shuffle(cards)
print(cards)