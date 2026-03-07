word = input("Enter word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")