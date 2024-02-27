# main.py RoboGarden Student Grade Tracker
# Demian Swindells 2/26/2024
# Build a program that helps students track their grades.
# Students can input the grades they achieve for each subject, and the program will read their grades from a file and calculate their average grade.
# The program should handle exceptions (e.g., invalid input, file errors) and store the grades in a file for future reference.

import pickle
print("Enter stop to terminate the program")
grade_book = {}

def dump():
    with open('grades.txt', "wb") as f:
        pickle.dump(grade_book, f)
    return

def add_entry(subject, grade):
    grade_book[subject] = grade
    dump()
    print(grade_book)
    return 

def display_avg():
    lngth = len(grade_book)
    grade_sum = sum(grade_book.values())
    avg = grade_sum / lngth
    print("Average Grade: ", avg)
    return

run = True
while run:
    try:
        subject = input("Please Enter Subject: ")
    except:
        print("Please enter the suject as a string.")
        continue
    if subject == "stop":
        run = False
        break
    else:
        try:
            grade = int(input("Please Enter the Grade for the Subject: "))
        except:
            print("Please enter the Grade as a positive Number")
            continue
        finally:
            if grade < 0:
                print("Please enter the Grade as positive number 0 or higher")
                continue
    add_entry(subject, grade)
    display_avg()