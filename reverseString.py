def reverse_string(s):
    result = ""
    for i in s:
        result = i + result
    return result

ask = input('type a word: ')
print(reverse_string(ask))