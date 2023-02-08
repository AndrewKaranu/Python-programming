import math

while True:
    menu_Options = "\nChoose an option\n\n1. Addition \n2. Subtraction\n3. Multiplication\n4. Division\n5. Remainder of a number\n6. Square Root of a Number\n7. Power of a Number\n8. Logarithm\n9. Sine\n10. Cosine\n11. Tangent\n\nEnter Your Choice: "

    # get the users choice
    user_choice= (input(menu_Options))
    
    # Addition
    if user_choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        sum = num1 + num2
        print(f"The sum of {num1} and {num2} is {sum}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    # Subtraction
    elif user_choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        diff = num1 - num2
        print(f"The difference between {num1} and {num2} is {diff}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    # Multiplication
    elif user_choice == "3":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        multi = num1 * num2
        print(f"The multiplication of {num1} and {num2} results in {multi}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    # Division
    elif user_choice == "4":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        div = num1 / num2
        print(f"{num1} divided by {num2} is {div}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    # Reamainder
    elif user_choice == "5":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        rem = num1 % num2
        print(f"The remainder of {num1} divided by {num2} is {rem}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
    else:
        print("Invalid Option. Please try again")