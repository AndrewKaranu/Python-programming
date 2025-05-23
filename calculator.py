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
    
    # Square root
    elif user_choice == "6":
        num1 = float(input("Enter the number you want to square root: "))
        sqrt = math.sqrt(num1)
        print(f"The square root of {num1} is {sqrt}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
        
    # Power of a number
    elif user_choice == "7":
        num1 = float(input("Enter the base number: "))
        num2 = float(input("Enter the power number: "))
        power = num1 ** num2
        print(f"{num1} to the power of {num2} is {power}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break
# Logaritms   
    elif user_choice == "8":
        base = input("Do you wish to specify the base of the Log? (Y) or (N): ")
        if base.lower() == "y":
            num1 = float(input("Enter the number you want to find the log of: "))
            num2 = float(input("Enter the base of the Log: "))
            log = math.log(num1,num2)
            print(f"The Log of {num1} is {log}")  
        else:
            num1 = float(input("Enter the number you want to find the log of: "))
        log = math.log(num1)
        print(f"The Log of {num1} is {log}")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break   
# Sine
    elif user_choice == "9":
        base = input("Would you like to calculate in degrees or radians? (D) or (R): ")
        if base.lower() == "d":
            num1 = float(input("Enter the number you want to find the Sine of: "))
            sin = math.sin(math.radians(num1))
            print(f"The Sine of {num1} is {sin} degrees")  
        else:
            num1 = float(input("Enter the number you want to find the Sine of: "))
            sin = math.sin(num1)
            print(f"The Sine of {num1} is {sin} radians")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break   
     # Cosine
    elif user_choice == "10":
        base = input("Would you like to calculate in degrees or radians? (D) or (R): ")
        if base.lower() == "d":
            num1 = float(input("Enter the number you want to find the Cosine of: "))
            cos = math.cos(math.radians(num1))
            print(f"The Cosine of {num1} is {cos} degrees")  
        else:
            num1 = float(input("Enter the number you want to find the Cosine of: "))
            cos = math.cos(num1)
            print(f"The Cosine of {num1} is {cos} radians")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break 
    # Tangent
    elif user_choice == "11":
        base = input("Would you like to calculate in degrees or radians? (D) or (R): ")
        if base.lower() == "d":
            num1 = float(input("Enter the number you want to find the Tangent of: "))
            tan = math.tan(math.radians(num1))
            print(f"The Tangent of {num1} is {tan} degrees")  
        else:
            num1 = float(input("Enter the number you want to find the Tangent of: "))
            tan = math.tan(num1)
            print(f"The Tangent of {num1} is {tan} radians")
        
        back = input("Do you wish to go back to the menu? (Y) or (N): ")
        if back.lower() == "y":
            continue
        else:
            break 
        
        
    else:
        print("\nInvalid Option. Please try again")