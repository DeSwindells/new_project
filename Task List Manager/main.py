# main.py RoboGarden Task List Manager
# Demian Swindells 2/27/2024
# Develop a simple task list manager that allows users to add, remove, and view tasks.
# The program should save the task list to a text file and handle exceptions in a controlled manner


print("Enter stop to terminate the program")
task_lst = []

def add_entry():
    task = input("Please input task to enter: ")
    task_lst.append(task)
    print("Task added Succesfuly")
    return 

def remove_entry():
    task = input("Please input task to remove: ")
    task_lst.remove(task)
    print("Task Removed Succesfuly.")
    return

def view_tasks():
    print(task_lst)
    return

def save_list():
    try:
        f = open("tasks.txt", 'a')
    except IOError:
        print("File Not Found")
    else:
        for x in range(len(task_lst)):
            f.write(task_lst[x] + '\n')
        f.close()
    print('List Saved Succesfully.')
    return

def load_list():
    try:
        f = open('tasks.txt', 'r')
    except IOError:
        print("File Not Found")
    else:
        print(f.readlines())
    return

run = True
while run:
    try:
        user_input = input("Please choose from the list: add, remove, view, save, load: ")
    except:
        print("Please enter the choise as a string.")
        continue
    if user_input == "stop":
        run = False
        break
    elif user_input == 'add':
        add_entry()
    elif user_input == 'remove':
        remove_entry()
    elif user_input == 'view':
        view_tasks()
    elif user_input == 'save':
        save_list()
    elif user_input == 'load':
        load_list()
    else:
        print('Please try again from the list.')
        continue

