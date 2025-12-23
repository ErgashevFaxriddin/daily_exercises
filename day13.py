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


def input_students_grouped():
    groups = {}

    while True:
        name = input("Enter student name (type 'stop' to finish): ")
        if name.lower() == "stop":
            break

        group = input("Enter student group: ")
        age = input("Enter student age: ")
        if age.isdigit():
            age = int(age)

        student = {
            'name': name,
            'age': age
        }

        # Add student to the correct group
        if group in groups:
            groups[group].append(student)
        else:
            groups[group] = [student]

    return groups

all_groups = input_students_grouped()

print("\nStudents by group:")
for grp, students in all_groups.items():
    print(f"Group {grp}:")
    for s in students:
        print(f"  Name: {s['name']}, Age: {s['age']}")
