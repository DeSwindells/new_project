# main.py RoboGarden Calculate Area
# Demian Swindells 2/23/2024
# Write a function to calculate the average of the numbers in a list of items using the built-in sum function
import random

rnd_lst = random.sample(range(0, 100), 10) # generates a list of 10 random numbers between 0 and 100
print("List of numbers: ", rnd_lst)

def calc_average(rnd_lst):
    lst_sum = sum(rnd_lst)
    lst_avg = lst_sum / len(rnd_lst)
    return lst_avg

avg = calc_average(rnd_lst)

print("The average of the list is: ", avg)
