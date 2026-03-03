# Sum of Even Numbers

numbers = [1, 2, 3, 4, 5, 6]

sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num

print("Sum of even numbers:", sum_even)