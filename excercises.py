# # num1 = 10
# # num2 = 2.5
# Var_type = ""

# def check_type(x)



# # # check the type of the variables
# # print(f"{num1} is a '{type}' number")
# # print(f"{num2} is a '{type}' number")

# # print(type(num1)) #integers
# # print(type(num2)) #float
# a = 1
# b = 2
# print(a == b) #-> == is the equality of the variables therefore output is false
# # print(b==c)

# a = "1"
# b = 2
# print(a + b)
# # expected output is 3
# print(int(a) + b)

# Write a python program that asks the user for their name and age then processes the input 
# and outputs the name of theage of the user alongside the users age in seconds

# Name = input("what is your name?")
# Age = input("What is your age?") # you can also convert the input into an integer

# print("Hello,{name},you have lived {years} years, {days} days, {hours} hours, {minutes} minutes and {age} seconds".format( name=Name, years=int(Age), days=int(Age)*365, hours=int(Age)*365*24, minutes=int(Age)*365*24*60, age=int(Age)*365*24*360))

import math
# Asks for radius and return the circumfrence

# Radius = float(input("What is the radius of the circle?"))

# print("With a radius of {radius} cm the circumfrence of the circle will be {circumfrence} cm and the area will be {area}cm\u00b2 \U0001f600.".format( radius=Radius, circumfrence=round(Radius*2*math.pi,0), area=round(Radius**2*math.pi,0)))
# \uoob2 is cm^2
# \U0001f600 is an example of a code for an emoji

# Make a python program that asks the user for their age and outputs the decades they have lived
Name = input("what is your name?")
Age = input("What is your age?") 
s = "s" if Age > "19" else "" #variable that changes between a decade and decades in the statement

print("Hello,{name},you have lived {years} decade{s}.".format( name=Name, years=int(Age)//10, s=s))