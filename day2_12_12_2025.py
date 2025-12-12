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


# # This exercise tests your ability to use multiple conditions and convert data types within the comprehension.
# # Task: Find all numbers from 1 to 1000 that are divisible by 8 and also contain the digit '6'.
# # Goal: Create a list containing numbers like 168, 264, etc.
# # Hint: You will need to convert the number to a string to check if "6" is in it.
# divisionable_numbers = [x for x in range(1, 1001) if x % 8 == 0 and "6" in str(x)]
# print(divisionable_numbers)


# # Task: Given a list of words, create a new list that includes only
# # the words that are longer than 3 letters and do NOT start with the letter 'P'.
# # The List: words = ["Apple", "Pie", "Pear", "Banana", "Kiwi", "Plum", "Orange"]
# # Goal: The result should be ['Apple', 'Banana', 'Kiwi', 'Orange']
# # (Note: "Pie", "Pear", and "Plum" are removed because they start with 'P').
# words = ["Apple", "Pie", "Pear", "Banana", "Kiwi", "Plum", "Orange"]
# filtered_words = [x for x in words if x.startswith('p'.title()) and len(x) > 3]
# print(filtered_words)


# Task: Take a string and create a list of its characters. If the character is a vowel (a, e, i, o, u),
# make it UPPERCASE. If it is a consonant, make it lowercase.
# Input String: text = "Python is Awesome"
# Goal: ['p', 'y', 't', 'h', 'O', 'n', ' ', 'I', 's', ' ', 'A', 'w', 'E', 's', 'O', 'm', 'E'] (ignoring spaces).
text = 'The Republic of Uzbekistan'
vowels = 'aeiouAEIOU'
solution = [x.upper() if x in vowels else x.lower() for x in text]
print(solution)