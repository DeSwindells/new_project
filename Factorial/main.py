# main.py RoboGarden Factorial
# Demian Swindells 2/15/2024
# Write a program that calculates the factorial of a number given by the user, then prints the output.

userNum = int(input("Please aenter a number to recieve the Factorial: "))# Receives User Number to Calculate Factorial

factorial = 1 # gives a default value to be able to multiply with (multiplying by 0 is 0)

if userNum < 0: # checks if the user entered a negative number (factorials require a positive number)
    print("There is no factorial for a negative number")
else:
    for n in range(1, userNum + 1): # loops from one up to the number entered by the user + 1 (cannot start factorial count at zero)
        factorial = factorial*n # multiplies the previous factorial number by the current loop iteration 
    print("The Factorial for the number: ", userNum, " is: ", factorial)