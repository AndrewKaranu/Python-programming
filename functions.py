# Functions/Normal trends
# A function is a block of code that performs a specific task when called
# Functions allow us to reuse code and not to repeat yourself(DRY-Dont Repeat Yourself)
# To create a function in python we start with the def keyword, then the name of the function, a pair of parenthesis followed by a colon
# After the colon you have to indent your code to tell pyhton that it belongs to the function block
# for a function to execute you need to call it. A function is called by writing its name followed by a pair of parenthesis

# A function that will great somebody
def great_User():
    print("Hello everyone")
# great_User()


# Create a function caleed "addTwoNumbers" that prints out the sum of any two numbers
# def addTwoNumber():
#     x = float(input("First number?"))
#     y = float(input("Second number?"))
#     sum = x+y
#     print(f"The sum is {sum}")
    
# addTwoNumber()

# Parameters and Arguments
# Parameter- Value you pass in the parenthesis of a function definition
# Argument- Value you pass to the function paranthesis when calling the function

# Create a function that takes in tow parameters and prints out their sum 
def addNumbers(x,y):
    sum = x+y
    print(f"The sum is {sum}")
   
# addNumbers(2,3)

# Create a function that takes in two numbers and prints out the square of the first number raised to the second number
# def square_Number(x,y):
#    num = x**2
#    power = num**y
#    print(f"The squared number is {power}")

def square_Number(x,y):
   num = x**y
   print(f"The squared number is {num}")
   
# square_Number(3,3)
    
# The return statement is used in a function to specify what value(s) to return to the caller of the function. It exits the function and sends a value back to the caller. The value can be any valid expression, such as a string, number, or list, for example

# Create a function that takes tow parameters and returns the square of the first number raised to the second number
def square(x,y):
   num = x**y
   return(f"The squared number is {num}")
   
# print(square(5,2))

# Namespaces-> Two types of namespaces nameley local and global
# Local-> the variables can be accessed inside of a method/function
# only-> these are variables that are created inside methods
# Global _> variables accessed globally (outside and inside function method.) -created outside a method


# Write a python program that asks the user for their name and age then processes the input and outputs the name of theage of the user alongside the users age in seconds

# def sec_Age():
#     Name = input("what is your name?")
#     Age = input("What is your age?") # you can also convert the input into an integer
#     return("Hello,{name},you have lived {years} years, {days} days, {hours} hours, {minutes} minutes or {age} seconds".format( name=Name, years=int(Age), days=int(Age)*365, hours=int(Age)*365*24, minutes=int(Age)*365*24*60, age=int(Age)*365*24*360))

# print(sec_Age())


# Create a function that will calculate the acceleration
# acceleration = v-u/t
# t1=0 t2=10
# v1=0
# v2=20

def acceleration(v1,v2,t1,t2):
    total_time= t2-t1
    velocity = v2-v1
    acc = velocity/total_time
    return acc

# print(acceleration(0,10,0,20))


# create a function that takes any string as input and returns the number of words in that for that string

# string1 = input("Write your sentence?")
# print(len(string1))
# print(string1.split())

def num_words(string):
   string_split = string.split(" ")
   words = len(string_split)
   return(words)

# print(num_words(string1))

def num_letters(string):
   space_del = (string.replace(" ",""))
   words = len(space_del)
   return(words)

# print(num_letters(string1))

# create a lottery app
# import random module
import random
# Create a function that creates the lottery numbers
def createLotteryNumbers():
    # values = []
    # for value in range(6):
    #     values.append(random.randint(1, 50))
    values = set()
    while len(values) < 6:
         values.add(random.randint(1, 50))
    return values
  

        
# Creat a function to get the lottery from the user

# def get_Player_Numbers():
#     numbers_csv = (input("Give your 6 numbers separated by a comma"))
#     six_numbers = numbers_csv.split(",")
#     print([(int(x) for x in six_numbers)]) ->comprehension
    
# get_Player_Numbers()

# or

def get_Player_Numbers():
    # int_numbers = []
    set_numbers = set()
    numbers_csv = (input("Give your 6 numbers separated by a comma: "))
    six_numbers = numbers_csv.split(",")
    # for number in six_numbers:
    #     int_numbers.append(int(number)) #-> converts the list elements into integers
    # print(int_numbers)
    for number in six_numbers:
        set_numbers.add(int(number)) #->converts the list elements into sets
    return set_numbers
        
# create the menu of our program

def menu():
    # ask the user for their numbers
    user_numbers = get_Player_Numbers()
    # Generate the lottery(winning) numbers
    lottery_numbers = createLotteryNumbers()
    # print out the winnings
    matched_number = user_numbers.intersection(lottery_numbers)
    money_won = (100**len(matched_number))
    print(f"The winning numbers were{lottery_numbers}and you matched {matched_number} and Won Kes{money_won}")
    

menu()

def menu():
    # ask the user for their numbers
    user_numbers = get_Player_Numbers()
    # Generate the lottery(winning) numbers
    lottery_numbers = createLotteryNumbers()
    # print out the winnings
    matched_number = user_numbers.intersection(lottery_numbers)
    money_won = (100**len(matched_number))
    print(f"The winning numbers were{lottery_numbers}and you matched {matched_number} and Won Kes{money_won}")