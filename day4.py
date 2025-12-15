# Step 1: Initialize the list of students and their grades
students_grades = [
    ("Alice", [80, 75, 90]),
    ("Bob", [60, 55, 70]),
    ("Charlie", [90, 85, 95]),
    ("David", [50, 45, 55]),
    ("Eve", [70, 65, 75])
]

# Step 2: Calculate the average grade for each student
students_with_avg = []
for name, grades in students_grades:
    avg_grade = sum(grades) / len(grades)
    students_with_avg.append((name, avg_grade))

# Step 3: Sort students by their average grade in descending order
students_with_avg.sort(key=lambda x: x[1], reverse=True)

# Step 4: Calculate the overall class average across all subjects
total_sum = sum(sum(grades) for _, grades in students_grades)
total_count = sum(len(grades) for _, grades in students_grades)
class_avg = total_sum / total_count

# Step 5: Filter out students who scored above the class average
above_class_avg = [student for student in students_with_avg if student[1] > class_avg]

# Step 6: Remove students with an average grade below 50
final_students = [student for student in students_with_avg if student[1] >= 50]

# Output the results
print("Sorted Students by Average Grade (Descending):")
for student in students_with_avg:
    print(f"{student[0]}: {student[1]:.2f}")

print("\nStudents Above Class Average:")
for student in above_class_avg:
    print(f"{student[0]}: {student[1]:.2f}")

print("\nFinal Students (Above or Equal to 50 Average):")
for student in final_students:
    print(f"{student[0]}: {student[1]:.2f}")