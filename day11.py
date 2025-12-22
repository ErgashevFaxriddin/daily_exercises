# day11 22/12/2025

# List all the keys and values of your dictionary.
# Add a new piece of information to your dictionary (like your favorite color).
# Update one value in your dictionary (for example, change your city).
# Delete one key-value pair from your dictionary.

# day 10 22/12/2025

import time
# Create a dictionary to store your personal information (name, age, city).


birth_year = 2004
concurrent_year = time.localtime().tm_year
age = concurrent_year - birth_year
my_info = {
    'name': 'faxriddin'.title(),
    'age': age,
    'city': 'Andijan'
}
for key, value in my_info.items():
    print(key, ': ', str(value).title() if isinstance(value, str) else value)
    if isinstance(value, int):
        print(value)

listed = [
    {
    'name': 'faxriddin'.title(),
    'age': age,
    'city': 'Andijan'
    }
]
listed[0]['color'] = 'green'
listed[0].update({'city': 'tashkent'})
del listed[0]['age']
print(listed)

for me in listed:
    for key, value in me.items():
        print(f"{key}: {value}")