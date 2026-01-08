#default arguments:
# A default value for certain parameters 

#There are 4 types of function in python:
# 1. Positional 2. Default 3. Keyword 4. Arbitary

#This program will be about default arguments 


def MassOfNeucleon(P , N, p = 1 , n = 1):
    mass = P*p + N*n
    return mass

Num_proton = int(input("Enter the number of proton: "))
Num_neutron = int(input("Enter the number of neutron: "))

print("Default mass of proton and neutron is 1 amu.")
choice = input("Do you want to change it(Y/N)? ")

if choice == "Y":
    mass_proton = float(input("Enter the mass of proton in amu: "))
    mass_neutron = float(input("ENter the mass of neutron in amu: "))

    Total_mass = MassOfNeucleon(Num_proton,Num_neutron,mass_proton,mass_neutron)
    print(f"The total mass of neucleon is: {Total_mass:02f} amu")

else:
    Total_mass = MassOfNeucleon(Num_proton,Num_neutron)
    print(f"The total mass of neucleon is: {Total_mass} amu")
