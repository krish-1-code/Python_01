# WAP a program to create a 2d number pad

# 1 2 3 
# 4 5 6 
# 7 8 9
# * 0 #

numberpad = (("1","2","3")
             ,("4","5","7")
             ,("7","8","9")
             ,("*","0","#"))

for rows in numberpad:
    for elements in rows:
        print(elements, end = " ")
    print()