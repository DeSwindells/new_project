# main.py RoboGarden Fibonacci
# Demian Swindells 2/13/2024
# Write a program to print the Fibonacci sequence for a count given by the user.

loopCount = 0
num1 = 0
num2 = 1
userCount = int(input("Please enter a number for the number of Fibonacci number you would like: ")) # Receive Input for user count

while loopCount < userCount: # Loops for the duration of the user count given
    loopCount += 1
    if loopCount == 0: # checks start of loop count and outputs first Fibonacci number
        print("Loop: ", loopCount, ", Fib: ", 0)
    elif loopCount == 1: # checks loop count and outputs second Fibonacci number
        print("Loop: ", loopCount, ", Fib: ", 1)
    else: # Calculates all other Fibonacci numbers for the sequence
        fib = num1 + num2
        num1 = num2
        num2 = fib
        print("Loop: ", loopCount, ", Fib: ", fib)
    



