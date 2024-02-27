# main.py RoboGarden 
# Demian Swindells 2/26/2024
# Create a simple personal diary application where users can write and save their daily thoughts or experiences to a text file.
# The program should allow users to view their previous entries and handle exceptions in a controlled manner (e.g., file not found errors and permission issues).

import datetime

def add_Entry(entry):
    try:
        f = open("diary.txt", 'a')
    except IOError:
        print("File Not Found")
    else:
        f.write(entry + '\n')
        f.close()
    return

def read_Entry():
    f = open("diary.txt", 'r')
    lines = f.readlines()
    print(len(lines))
    for x in range(len(lines)):
        print(lines[x])
    f.close()

def add_TimeStamp():
    f = open("diary.txt", 'a')
    f.write(str(datetime.datetime.now()) + "\n")
    f.close()

optn_list = ["entry", "read", "timestamp", "close"]

run = True
while run:
    print("Please type what you would like to do from the list: ")
    print(optn_list)
    choice = input()

    if choice == "entry":
        entry = input("Please enter a line to enter into the Diary: ")
        add_Entry(entry)
    elif choice == ("read"):
        read_Entry()
    elif choice == 'timestamp':
        add_TimeStamp()
    else:
        run = False