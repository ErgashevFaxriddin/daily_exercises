# # day 13 23/12/2025
#
# def input_students():
#     students = []
#
#     while True:
#         name = input("Enter student name (type 'stop' to finish): ")
#         if name.lower() == "stop":
#             break
#
#         group = input("Enter student group: ")
#         age = input("Enter student age: ")
#         if age.isdigit():
#             age = int(age)
#
#         student = {
#             'name': name,
#             'group': group,
#             'age': age
#         }
#
#         students.append(student)
#
#     return students

#
# def input_students_grouped():
#     groups = {}
#
#     while True:
#         name = input("Enter student name (type 'stop' to finish): ")
#         if name.lower() == "stop":
#             break
#
#         group = input("Enter student group: ")
#         age = input("Enter student age: ")
#         if age.isdigit():
#             age = int(age)
#
#         student = {
#             'name': name,
#             'age': age
#         }
#
#         # Add student to the correct group
#         if group in groups:
#             groups[group].append(student)
#         else:
#             groups[group] = [student]
#
#     return groups
#
# all_groups = input_students_grouped()
#
# print("\nStudents by group:")
# for grp, students in all_groups.items():
#     print(f"Group {grp}:")
#     for s in students:
#         print(f"  Name: {s['name']}, Age: {s['age']}")
#
#
#

def input_advanced_students():
    groups = {}

    while True:
        name = input("Enter student name (type 'stop' to finish): ")
        if name.lower() == "stop":
            break

        group = input("Enter student group: ")

        # Age input with validation
        while True:
            age = input("Enter student age: ")
            if age.isdigit():
                age = int(age)
                break
            else:
                print("Age must be a number. Try again.")

        # Scores input for multiple subjects
        scores = {}
        while True:
            subject = input("Enter subject name (type 'stop' to finish subjects): ")
            if subject.lower() == "stop":
                break
            while True:
                score = input(f"Enter score for {subject}: ")
                if score.isdigit():
                    scores[subject] = int(score)
                    break
                else:
                    print("Score must be a number. Try again.")

        # Calculate average score
        avg_score = sum(scores.values()) / len(scores) if scores else 0

        student = {
            'name': name,
            'age': age,
            'scores': scores,
            'average_score': avg_score
        }

        # Add student to group
        if group in groups:
            groups[group].append(student)
        else:
            groups[group] = [student]

    return groups


all_groups = input_advanced_students()

print("\nStudents by group (sorted by average score descending):")
for grp, students in all_groups.items():
    print(f"\nGroup {grp}:")
    # Sort students by average score descending
    students_sorted = sorted(students, key=lambda s: s['average_score'], reverse=True)

    group_avg = sum(s['average_score'] for s in students_sorted) / len(students_sorted) if students_sorted else 0
    print(f"Average score for group: {group_avg:.2f}")

    for s in students_sorted:
        print(f"  Name: {s['name']}, Age: {s['age']}, Average Score: {s['average_score']:.2f}, Scores: {s['scores']}")
