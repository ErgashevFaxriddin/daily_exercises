# Range Extraction: Generate a list of all numbers from 0 to 50 that are divisible by 5.

# numbers = [x for x in range(1, 51) if x % 5 == 0]
# print(numbers)


# String Lengths: Given a list of words, create a list containing the length (number of characters) of each word

# words = ['apple', 'banana', 'tree', 'life', 'cherry']
# count = [len(word) for word in words]
#
# combined = [(words[i], count[i]) for i in range(len(words))]

# print(combined)


# list1 = [1, 2, 3]
# list = ['a', 'b']
# list1.extend(list)
# print(list1)

# x = ('apple', 'banana', 'kiwi')

# y = list(x)
# y.append('cherry')
# y.remove('kiwi')
# x = tuple(y)

# x = tuple([y for y in x if y != 'kiwi'] + ['cherry'])

# print(x)
#
# #
# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):
# #   # print(thistuple[i])
#
# thistuple = ("apple", "banana", "cherry")
# for x in thistuple:
#     print(x)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)


# mytuple = (1, 2, 3)
# a, b, c = mytuple


# numbers = (10, 20, 30)
# a, b, c = numbers


# a = (1, 2, 3)
# b = (4, 5, 6)
# c = a + b
# print(c)


# t = (0,1)
# t2 = t * 5
# print(t2)


# numbers = (1, 2, 3, 4, 5)
# a, *b = numbers


# logs = [(12,"Ali",5000), (15,"Bob",7000)]
# for t in logs:
#     truck, driver, load = t
#     print(truck, driver, load)

#
# nested = (1,(2,(3,4),5),6)
#
# for t in nested:
#     a, b = t  # unpack each inner tuple
#     print(a, b)


nested = (1, (2, (3, 4), 5), 6)

for t in nested:
    if isinstance(t, tuple) and len(t) == 2:
        a, b = t
        print(a, b)
