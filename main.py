from even_odd import even_odd_funtion
from guess_number import guess_num

while True:
    choice = input("WHICH GAME DO YOU PLAY?\n1 - GUESS THE NUMBER\n2 - EVEN/ODD\nEnter 1 OR 2: ")

    if choice == '1':
        guess_num()
    elif choice == '2':
        even_odd_funtion()
    else:
        print("PLEASE ENTER 1 OR 2!")

    again = input("DO YOU WANT TO PLAY AGAIN? (1/0): ")
    if again != '1':
        print("GOODBYE!")
        break
