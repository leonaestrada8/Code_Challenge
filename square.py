import math
start=""

while True:
    # Prompt user for input
    if start != "over":
        input_num = input("Enter an integer: ")

    # Check if input is valid integer
    try:
        input_num = int(input_num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.\n")
        continue
    
    # Check if input is a square number
    square_root = int(math.sqrt(input_num))
    if  input_num >= 0 and square_root ** 2 == input_num:
        print()
        print(f"============>>>> {input_num} IS A SQUARE NUMBER!\n")
    else:
        print(f"{input_num} is not a square number.\n")

    # Ask user if they want to enter another integer
    again = input("Would you like to enter another integer? (y/n or another integer) \n")
    try:
        input_num = int(again)
        start="over" 
    except ValueError:
        if again.lower() not in ['y', 'yes']:
            start=""
            break
        else:
            start=""