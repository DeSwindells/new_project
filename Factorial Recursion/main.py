# main.py RoboGarden Factorial Conversion
# Demian Swindells 2/20/2024
# Write a function to calculate factorials using recursion.

def calc_factorial(userNumb):# recursive Factorial Function
    if userNumb == 1:
        return userNumb
    else:
        return userNumb*calc_factorial(userNumb-1) # Recursive Statement

userNumb = int(input("Please enter a number to recieve the Factorial"))
if userNumb < 0:
    print("Negative numbers cannot have a factorial")
elif userNumb == 0:
    print("The Factorial of 0 is 1")
else:
    print("The Factorial of ", userNumb, " is ", calc_factorial(userNumb))