# # 5
# numbers = [4, 1, 7, 3, 8]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)


# 6
# quadrates = [x**2 for x in range(1, 6)]
# print(quadrates)


# # even numbers
# even_numbers = [x for x in range(1,11) if x % 2 != 0]
# print(even_numbers)


# # Task: Given a list of names, names = ["Alice", "Bob", "Charlie", "David"], create a new list that contains only the first letter of each name.
# # Goal: Create a list like ['A', 'B', 'C', 'D'].
# names = ["Alice", "Bob", "Charlie", "David"]
# letters = [x[0] for x in names]
# print(letters)


# # first letters as a FUNCTION
# def get_first_letters(name_list):
#     return [name[0] for name in name_list]
#
# ismlar = ['Ali', 'Bahrom', 'Jasur']
# print(get_first_letters(ismlar))


# This exercise tests your ability to use multiple conditions and convert data types within the comprehension.
# Task: Find all numbers from 1 to 1000 that are divisible by 8 and also contain the digit '6'.
# Goal: Create a list containing numbers like 168, 264, etc.
# Hint: You will need to convert the number to a string to check if "6" is in it.
divisionable_numbers = [x for x in range(1, 1001) if x % 8 == 0 and "6" in str(x)]
print(divisionable_numbers)