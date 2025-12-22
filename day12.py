# day 12 22/12/2025
# You are given a dictionary where keys are student names and values are lists of their grades. For example, "Alice": [85, 90, 78].
# Tasks:
# Calculate the average grade for each student and store it in a new dictionary.
# Determine which student has the highest average.
# Identify all students who scored below 80 in any subject.
# Print a summary showing each student’s grades, average, and whether they passed (assume passing is average ≥ 80).

# Challenge:
# Try to solve it without using external libraries.
# Make your solution dynamic, so it works if more students are added.

students = [85, 90, 78, 23, 43, 100]
average = sum(students) / 2
print('average: ', average)

max_students = max(students)
print(max_students)