item_name = input("Enter the name of the item: ")
number = int(input(f"how many {item_name} you want: "))
price = 4.99
total = number * price
total = round(total,2)
print(f"You bought {number} {item_name}")
print(f"Your total for {number} {item_name} is {total}")