# Objective:
# The aim of this assignment is to integrate various list operations and methods to solve a complex problem.

# Problem Statement:
# You're organizing a school event, and you have lists containing student names, their grades, and the activities they're interested in.

# Task 1: Given the lists:

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

# Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"
students_below_80_indexes=[]
for i in range(0,len(grades)):
    if grades[i] < 80:
        students_below_80_indexes.append(i)

if len(students_below_80_indexes) > 0:
    for index in students_below_80_indexes:
        print(students[index], grades[index], activities[index], sep=", ")
else:
    print("No Students with grade lower than 80")

# Task 2: For the remaining students, add students name in a new list named students_approved. Expected Outcome: students_approved = ["John", "Doe", "Smith"]

# I could modify the task 1 code to add students are above 80 to students_approved

students_below_80_indexes=[]
students_approved=[]

for i in range(0,len(grades)):
    if grades[i] < 80:
        students_below_80_indexes.append(i)
    else:
        students_approved.append(students[i])

# Task 3: Print the list students_approved

print(students_approved)
