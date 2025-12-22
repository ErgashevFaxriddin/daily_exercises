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