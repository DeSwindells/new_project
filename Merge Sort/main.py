# main.py RoboGarden Merge Sort
# Demian Swindells 2/18/2024
# Merge-sort first divides the array into equal halves, then combines them in a sorted manner.
# Write a program that sorts the array using merge-sort algorithm.
import random

rnd_lst = random.sample(range(0, 100), 10) # generates a list of 10 random numbers between 0 and 100
print("Unsorted List: ", rnd_lst)

def mergeSort(arr):
    if len(arr) > 1:
 
         # Finding the mid of the array
        split = len(arr)//2
 
        # Dividing the array elements
        lst1 = arr[:split]
 
        # Into 2 halves
        lst2 = arr[split:]
 
        # Sorting the first half
        mergeSort(lst1)
 
        # Sorting the second half
        mergeSort(lst2)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                arr[k] = lst1[i]
                i += 1
            else:
                arr[k] = lst2[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(lst1):
            arr[k] = lst1[i]
            i += 1
            k += 1
 
        while j < len(lst2):
            arr[k] = lst2[j]
            j += 1
            k += 1

mergeSort(rnd_lst)

print("Sorted List: ", rnd_lst) # prints sorted list
