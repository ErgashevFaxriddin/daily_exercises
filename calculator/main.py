from plus import add

print("WELCOME TO CALCULATOR")

while True:
    print("\nCHOOSE:")
    print("1 - ADD")
    print("0 - EXIT")
    choice = input("Enter choice: ")

    if choice == '1':
        add()
        cont = input("CONTINUE? (1 = YES / 0 = NO): ")
        if cont == '0':
            break
    elif choice == '0':
        break
    else:
        print("INVALID CHOICE. TRY AGAIN.")

print("THANK YOU!")
