#using time library create a counter

import time

#we will use the sleep function of time library to get the delay we want.

mytime = int(input("Enter the seconds timer: "))

for i in range(mytime,0,-1):
    sec = i%60
    print(f"00:00:{sec:02}")
    time.sleep(1)

print("Happy new year cutieji")