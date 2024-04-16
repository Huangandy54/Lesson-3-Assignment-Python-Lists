# Objective:
# The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement:
# You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract the temperatures for the second week (7 days) of the month. Expected Outcome:
# 83, 85, 86, 87, 88, 89, 90,

print(temperatures[7:14])

# Task 2: Extract all the temperatures above 100.

# since the temperature list is sorted, we can find the first occurance of a temp > 100
index=None
for i in range(0, len(temperatures)):
    if temperatures[i] >100:
        index=i
        break
if index is not None:
    temperatures_above_100=temperatures[index:]
    print(temperatures_above_100)
else:
    print("No Temperatures above 100")

# Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.

temperatures.reverse()
print(temperatures[4:10])