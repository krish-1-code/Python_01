#TO FIND THE LENGTH USE LEN FUNCTION

name = "krish r"

length = len(name)
print(length)

#TO FIND THE INDEX OF ANY LETTER

index = name.find("r")
print(index)

#TO FIND THE LAST OCCURENCE POSITION OF AN CHARACTER

index = name.rfind("r")
print(index)

#TO CAPILTALIZE THE FIRST LETTER OF AN STRING:

capt = name.capitalize()
print(capt)

#FOR UPPER AND LOWER CASE:

upp = name.upper()
print(upp)

loww = name.lower()
print(loww)

#TO CHECK IF THE STRING IS AN DIGIT:

NUM = "122456"
outcome = NUM.isdigit()
outcome2 = name.isalpha()
print(outcome)
print(outcome2)

#WAP TO COUNT ANY OCCUERNECE:

number = "9864845199"
occ = number.count("9")
print(occ)

#REPLACE ANY CHARACTER

name = "Jeffrey epstein"
new_name = name.replace("Jeffrey","----")
print(new_name)
