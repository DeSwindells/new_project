# main.py RoboGarden Bubble Sort
# Demian Swindells 2/18/2024
# Bubble sort is a comparison-based algorithm in which each pair of adjacent elements is compared and swapped, if they are not in order.
# Write a program that sorts an array ascendingly using bubble sort.
import random

rnd_lst = random.sample(range(0, 100), 10) # generates a list of 10 random numbers between 0 and 100
print("Unsorted List: ", rnd_lst)

for n in range(len(rnd_lst)-1, 0, -1): # loops through the length of the random list 
    for i in range(n): # loops for every remaining iteration of the list
        if rnd_lst[i] > rnd_lst[i + 1]: # compares the current list item to the one after it
            rnd_lst[i], rnd_lst[i + 1] = rnd_lst[i + 1], rnd_lst[i] # swaps the current list item with the one after it
print("Sorted List: ", rnd_lst) # prints sorted list
