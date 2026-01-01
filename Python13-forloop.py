# WAP to print table of number given by user

#for loop in python is not as straight forward as in C
#atleast in my opinion

# For loops execute a block of number a fix number of times 
#while is prefered when there is not fixed iteration as we saw in the examples of while loop

#for loop can iterate over range; string; sequence

# let's start with range and the classic

#WAP to print 1 - 10

#for i in range (1,10):
#    print(i)

#one thing to notice is last range is exclusive 
# no intead on 1 to n ; 1 to n+1


#WAP to print first 10 odd numbers

#for i in range(2,21,2):
#    print(i)

#WAP to iterate over string 

phone_num = "605-671-8620"
for i in phone_num:
    if i == "-":
        continue
    else:
        print(i)