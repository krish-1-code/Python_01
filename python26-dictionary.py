#this is the 4th type of collection
# dictionary is a collection of {key:value} pairs
# they are ordered and changeable but no duplicates

capital = {"US": "DC",
           "India" : "Delhi",
           "Russia": "Moscow"}

#to get the name of one capital

#print(capital.get("US"))
#print(capital.get("Japan")) #output will be none

#this none feature can also be used in if statement

#country = input("Whose capital you want: ")

#if capital.get(country):
  #  print(capital.get(country))
#else:
 #   print("That country doesn't exist")

#To add any key to our dictionary

capital.update({"Japan":"Tokyo"})

print(capital)

#To remove any key

capital.pop("India")

print(capital)

# To remove the last key that was added

capital.popitem()

print(capital)

#To print only the keys and not the values

print(capital.keys())

# key method is iterable

for key in capital.keys():
    print(key)

# just like keys you can use values

print(capital.values())

# what if we have to print both key and value:

print(capital.items())

#if we use it as iterable then it will be helpful:

for key,item in capital.items():
    print(f"{key:10} : {item}")


