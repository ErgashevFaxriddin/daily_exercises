# Import the 'operator' module, which provides functions for common operations like sorting.
import operator

# Create a dictionary 'd' with key-value pairs.
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

# Print the original dictionary 'd'.
print('Original dictionary : ', d)

# Sort the items (key-value pairs) in the dictionary 'd' based on the values (1st element of each pair).
# The result is a list of sorted key-value pairs.
sorted_d = sorted(d.items(), key=operator.itemgetter(1))

# Print the dictionary 'sorted_d' in ascending order by value.
print('Dictionary in ascending order by value : ', sorted_d)

# Convert the sorted list of key-value pairs back into a dictionary.
# The 'reverse=True' argument sorts the list in descending order by value.
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))

# Print the dictionary 'sorted_d' in descending order by value.
print('Dictionary in descending order by value : ', sorted_d) 