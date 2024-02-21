# main.py RoboGarden Fibonacci Recursion
# Demian Swindells 2/20/2024
# Write a program to print the Fibonacci sequence for a count given by the user using a recursive function.

userCount = int(input("Please enter a number for the number of Fibonacci number you would like: ")) # Receive Input for user count

def fib_recursion(userCount):
    if userCount <= 1:
        return userCount
    else:
        return(fib_recursion(userCount-1) + fib_recursion(userCount-2))
if userCount <= 0:
    print("Please enter an Integer 2 or higher")
else:
    for i in range(userCount):
        print(fib_recursion(i))
    
