# main.py RoboGarden Prime Numbers
# Demian Swindells 2/15/2024
# Write a program to print all the Prime Numbers between 2 and a number (N) given by the user.

userNum = int(input("Please enter a number larger than 2 for a range of prime numbers"))

for num in range(0, userNum): # loops for the length of the given user input
    if num > 1: # checks if the number is greater than 1 (only positive numbers can be prime)
        for i in range(2, num):
            if(num % i) == 0: # checks if the number is a prime number
                 break
        else:
            print(num) # prints the prime number
