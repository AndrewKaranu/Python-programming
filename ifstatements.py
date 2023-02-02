# Python Conditionals if/elif/else
# Indentation->
# If statement->
# lets use the if statemnt to execute a block of code. If the expression we provide will be evaluated as true
x = 10 
if x > 5:
    print(f"{x} is greater than 5")
    print(x * 2)       #-> As long a sthe statemnt is true all the code in the block will be executed
print(x * 3)

# if - else statements
# write a program that checks the temperature provided by the user:if the tem exceeds 32, then display "Cover tomatos", Otherwise "uncover tomatos"

# temp = float(input("what is the temperature:"))
# if temp > 32:
#     print("Cover tomatoes")
# else:
#     print("Uncover tomatoes")
    
    
# What if you want to handle multiple cases. lets say you want something to be printed out regardless of the true or false result of the evaluation
# For this you will use the elif or else statements

# Lets print "x is greater than 5" if "x" is indeed greater than 5, and "x is NOT greater than 5" in any other case
x = 4
if x > 5:
    print(f"{x} is greater than 5")
else:
    print(f"{x} is less than 5")
    
# The else statement is used to cover all the other  not covered by the it statement above it. If the expression following the it keyword is true the indented code below it will be executed. Otherwise if the expression is evaluated as false, the indented code below else gets executed. 

# Elif
# What if we want to be more granular and specify more cases and possible outputs in our program.Then we wil use an elif staement.
# Lets say we want to print "x is greater than 5" if "x" is indeed greater than 5, "x is equal to 5" in case x will become = to 5 at some point and "x is less than 5" in any other 

# The elif statement should be between if and else
# The else statement should always be the lats statement in and if elif else block

x = 5
if x > 5:
    print(f"{x} is greater than 5")
elif x == 5:
    print(f"{x} is equal to 5")
else:
    print(f"{x} is less than 5")
    

# # Database
# user_name = "Andrew"
# user_password = "secret"
    
# # Getting the user data
# print("\t\t\t\t\tLogin System")
# user_n = input("What is your username?")
# user_p = input("What is your password?")
    
#     # check if username and password match
# if user_n == user_name and user_p == user_password:
#     print("You are logged in!")
# else:
#     print("Incorect credentials")
     
     
# write a python program to wheck if a number even or odd
x = int(input("Input a number:"))

if x % 2 == 0:
    print("even")
elif x % 2 > 0:
    print("odd")
else:
    print("invalid number")

    
    
    
    
   
    
    
    
    
    
    
    