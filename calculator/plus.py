def add():
    while True:
        num1 = input("FIRST NUMBER: ")
        num2 = input("SECOND NUMBER: ")

        # Check if input is whole number
        if not num1.isdigit() or not num2.isdigit():
            print("THIS IS NOT A WHOLE NUMBER. TRY AGAIN.")
            continue

        # Convert to integers
        num1 = int(num1)
        num2 = int(num2)

        # Add numbers
        result = num1 + num2
        print("RESULT:", result)
        break  # exit loop after successful addition
