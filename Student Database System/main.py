# main.py RoboGarden Student Database System
# Demian Swindells 2/28/2024
# Create a simple student database system that stores information about students, such as their names, ages, and grades.
# Use classes to represent students and include methods for displaying student information and calculating average grades.

class Student:
 
  # Constructor
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
 
    # Function to create and append new student
    def add_student(self, Name, age, grades):
        ob = Student(Name, age, grades)
        ls.append(ob)
 
    # Function to display student details
    def display_info(self, ob):
        print("Name : ", ob.name)
        print("Age : ", ob.age)
        print("Grades : ", ob.grades)
        print("\n")
 
    # Calculate Average
    def avg(self, ob):
        sum = ob.grades
        return sum
 
# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0)
grades = [3]
run = True
while run:
    user_input = input("Enter choice: stop, add, avg, display: ")

    if user_input == 'add':
        name = input("please enter a name: ")
        age = int(input("please enter an age: "))
        for x in range(0, 3):
            grades = []
            grade = int(input("please enter grade: "))
            grades.append(grade)
        obj.add_student(name, age, grade)
        continue
    
    elif(user_input == 'display'):
        print("\n")
        print("\nList of Students\n")
        for i in range(ls.__len__()):
            obj.display_info(ls[i])
        continue
    
    elif(user_input == 'avg'):
        sum = 0
        print("\n Student Average, ")
        for i in range(ls.__len__()):
            sum = sum + obj.avg(ls[i])
        avg = sum / ls.__len__()
        print(avg)
        continue
    elif user_input == 'stop':
        run = False
        break
    else:  
        print("Thank You !")