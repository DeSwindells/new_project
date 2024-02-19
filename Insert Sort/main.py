# main.py RoboGarden Insert Sort
# Demian Swindells 2/19/2024
# The Insertion-sort function involves finding the correct place for a given element in a sorted list
# Write a program that sorts an array using the insertion-sort algorithm.

import random

rnd_lst = random.sample(range(0, 100), 10) # generates a list of 10 random numbers between 0 and 100
print("Unsorted List: ", rnd_lst)

for i in range(1, len(rnd_lst)): # loops through the length of the list
    key = rnd_lst[i] # stores the current item value as a key
    j = i-1
    while j >= 0 and key < rnd_lst[j]: # moves 
        rnd_lst[j + 1] = rnd_lst[j]
        j -= 1
    rnd_lst[j + 1] = key
print("Sorted List: ", rnd_lst) # prints sorted list
    