# ---------------------------
# Python Dictionary Exercises
# ---------------------------

# 1. Create a dictionary
student = {"name": "Ali", "age": 20, "grade": "A"}
print("1. Initial student dictionary:", student)

# 2. Access values
print("2. Student name:", student["name"])
print("   Student grade:", student["grade"])

# 3. Add a new key-value pair
student["city"] = "Tashkent"
print("3. Added city:", student)

# 4. Update a value
student["age"] = 21
print("4. Updated age:", student)

# 5. Delete a key-value pair
del student["grade"]
print("5. Removed grade:", student)

# 6. Loop through dictionary
print("6. Looping through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# 7. Check if a key exists
if "grade" in student:
    print("7. Found grade")
else:
    print("7. Grade not found")

# 8. Merge dictionaries
extra_info = {"hobby": "reading", "language": "English"}
student.update(extra_info)
print("8. After merging extra_info:", student)

# 9. Sum values in dictionary
scores = {"math": 90, "english": 80, "history": 70}
total_score = sum(scores.values())
print("9. Total score:", total_score)

# 10. Dictionary comprehension
squared = {x: x**2 for x in range(1, 6)}
print("10. Squared numbers dictionary:", squared)

# ---------------------------
# Complete Dictionary Example
# ---------------------------

# Step 1: Create a dictionary for a student
student = {"name": "Ali", "age": 20, "grade": "A", "math": 90, "english": 80, "history": 70}
print("Initial student dictionary:", student)

# Step 2: Update some values
student["age"] = 21            # Update age
student["city"] = "Tashkent"   # Add a new key-value pair
print("\nAfter updating age and adding city:", student)

# Step 3: Remove a key
del student["grade"]
print("\nAfter removing grade:", student)

# Step 4: Loop through dictionary and print keys & values
print("\nStudent information:")
for key, value in student.items():
    print(f"{key}: {value}")

# Step 5: Check if a key exists
key_to_check = "grade"
if key_to_check in student:
    print(f"\nKey '{key_to_check}' exists.")
else:
    print(f"\nKey '{key_to_check}' does not exist.")

# Step 6: Merge another dictionary
extra_info = {"hobby": "reading", "language": "English"}
student.update(extra_info)
print("\nAfter merging extra_info:", student)

# Step 7: Calculate total score (sum of numeric values)
numeric_keys = ["math", "english", "history"]
total_score = sum(student[key] for key in numeric_keys)
print("\nTotal score:", total_score)

# Step 8: Create a new dictionary using comprehension
squared_numbers = {x: x**2 for x in range(1, 6)}
print("\nSquared numbers dictionary:", squared_numbers)

# ---------------------------
# Complete Dictionary Program
# ---------------------------

# Create a dictionary for a student
student = {
    "name": "Ali",
    "age": 20,
    "grades": {"math": 90, "english": 80, "history": 70},
    "city": "Tashkent"
}

print("Initial student dictionary:")
print(student)

# Update values
student["age"] = 21                 # Update age
student["grades"]["math"] = 95      # Update a nested value
student["hobby"] = "reading"        # Add new key
print("\nAfter updates:")
print(student)

# Delete a key
del student["city"]
print("\nAfter deleting city:")
print(student)

# Loop through dictionary
print("\nLooping through student dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# Check if a key exists
if "grades" in student:
    print("\nGrades key exists.")
else:
    print("\nGrades key does not exist.")

# Merge another dictionary
extra_info = {"language": "English", "sport": "football"}
student.update(extra_info)
print("\nAfter merging extra_info:")
print(student)