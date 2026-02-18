from curses.ascii import isdigit


def add(num1, num2):
    while True:
        num1 = int(input('FIRST NUMBER: '))
        num2 = int(input('SECOND NUMBER: '))
        if num1 or num2 is not isdigit(num1):
            print('THIS IS NOT A NUMBER')
            continue

        elif float(num1) or float(num2):
            print('PRINT AN EVEN NUMBER')
            continue

        else:
            continue