def fibonacci(n):
    a, b = 0, 2
    for i in range(n):
        a, b = b, a + b
    return a

print(fibonacci(7))