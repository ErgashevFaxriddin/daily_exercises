# string

# b = 'hello world!'
# print(b[2:5])

# b = "Hello, World!"
# print(b[-5:-2])

# positive index
# 1, 2, 3, 4, 5
# -5, -4, -3, -2, -1

# txt = 'hello world!'
# txt2 = 'bye world!'
# print(txt.casefold(), txt2)

# thisset = {"apple", "banana", "cherry"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", "apple"}
# print(thisset)

# thisset = {"apple", "banana", "cherry", True, 1, 2}
# print(thisset)

# thisset = {'mango', 'lemons', 'dragon-fruits'}
# print('banana' not in thisset)

# thisset = {'mango', 'lemons', 'dragon-fruits'}
# print('banana' not in thisset)

# thisset = {'orange', 'banana', 'mango', 'dragon-fruits'}
# thisset.add('apple')
# print(thisset)

# thisset = {'orange', 'banana', 'mango', 'dragon-fruits'}
# melon_crops = {'melon', 'watermelon', 'winter melon'}
# thisset.update(melon_crops)
# print(thisset)

# set1 = {'one', 'two', 'three'}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)

# set1 = {'one', 'two', 'three'}
# set2 = {1, 2, 3}
# set3 = {'Anna', 'Selena', 'Andry'}
# myset = set.union(set1, set2, set3)
# print(myset)

set1 = {'one', 'two', 'three'}
set2 = {1, 2, 3}
set3 = {'Anna', 'Selena', 'Andry'}
myset = set1 | set2 | set3
print(myset)