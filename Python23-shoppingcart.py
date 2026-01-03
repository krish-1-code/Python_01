
foods = []
prices = []
total = 0

while True:
    food = input("Enter the food name. Press q to exit: ")

    if food.lower() == "q":
        break

    price = float(input("Enter the price: $"))
    
    foods.append(food)
    prices.append(price)

print("------------------------------")
print("You bought")

for item in foods:
    print(item, end = " ")

for cost in prices:
    total += cost

print()
print(f"The total cost is ${total}")