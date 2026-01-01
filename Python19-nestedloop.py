# A loop inside a loop

# In this program we'll be using nested loop to make some patterns


# 1 2 3 4
# 1 2 3 4
# 1 2 3 4 
# 1 2 3 4

for i in range(1,5):
    for j in range(1,5):
        print(j, end=" ")
    print() # for line break

# *
# **
# ***
# ****
# *****

for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()