# Objective:
# The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.

# Problem Statement:
# You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Find out which students both submitted their assignments and attended the class.
both=[student for student in submitted if student in attended]

print(both)

# Task 2: Check if the two lists are identical in terms of their content, regardless of order.

if sorted(submitted)==sorted(attended):
    print(True)
else:
    print(False)

# Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.

# I think this not using only list method?
# attended=[student for student in attended if student in submitted]

for student in attended.copy():
    if student not in submitted:
        attended.remove(student)

print(attended)