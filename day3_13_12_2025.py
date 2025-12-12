# Range Extraction: Generate a list of all numbers from 0 to 50 that are divisible by 5.

numbers = [x for x in range(1, 51) if x % 5 == 0]
# print(numbers)


# String Lengths: Given a list of words, create a list containing the length (number of characters) of each word

words = ['apple', 'banana', 'tree', 'life', 'cherry']
count = [len(word) for word in words]

combined = [(words[i], count[i]) for i in range(len(words))]

print(combined)