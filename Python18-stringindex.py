# Let's learn string indexing 

phone = "986-484-5199"

#string indexing has 1. starting point : end point : steps

print(phone[0:]) #from start to end

print(phone[0:11]) # has startand end point

print(phone[:5]) # 0 to 5

print(phone[::2]) # 2 steps 1,3,5,7,9

print(phone[-1]) # last number

print(f"XXX-XXX-{phone[-4:]}")

print(phone[-1::-1]) # to reverse a string