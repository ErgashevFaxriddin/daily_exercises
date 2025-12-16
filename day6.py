# Dictionary

# data = dict(name='ali', city='tashkent')
# print(data.get('name'))

# car = dict(mode='lamborhini', year=2025)
# x = car.items()
# print(x)

# car = dict(mode='lamborhini', year=2025)
# car.pop('year')
# print(car.items())

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.clear()
# print(thisdict)

# students = {
#     'george': 21,
#     'Anna': 23,
#     'lily': 10,
#     'asad': 33,
#     'begali': 42
# }
# for key, value in students.items():
#     print(f"Student {key.title()} {value} years old!")

# students = {
#     'george': 21,
#     'Anna': 23,
#     'lily': 10,
#     'asad': 33,
#     'begali': 42
# }
# a = [x if x > 18 else "Too young" for x in students.values()]
# print(a)

# Check if a key exists
#
# Check if “Sara” exists in the dictionary.
#
# Print a message based on the result.
students = {
    "Ali": 18,
    "Anna": 20,
    "John": 19,
    'sarah':12
}

result = [name for name in students if name.lower() == "sarah"]

print(result[0] if result else "there is no sarah")
