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

# import math
# # Asks for radius and return the circumfrence

# Radius = float(input("What is the radius of the circle?"))

# print("With a radius of {radius} cm the circumfrence of the circle will be {circumfrence} cm and the area will be {area}cm\u00b2 \U0001f600.".format( radius=Radius, circumfrence=round(Radius*2*math.pi,0), area=round(Radius**2*math.pi,0)))
# \uoob2 is cm^2
# \U0001f600 is an example of a code for an emoji

# Make a python program that asks the user for their age and outputs the decades they have lived
# Name = input("what is your name?")
# Age = input("What is your age?") 
# s = "s" if Age > "19" else "" #variable that changes between a decade and decades in the statement

# print("Hello,{name},you have lived {years} decade{s}.".format( name=Name, years=int(Age)//10, s=s))

# Write a python prgram that asks the user for scores of 5 subjects and outputs the average score


# Name = input("what is your name?")
# Math = float(input("What is your math grade?"))
# Physics = float(input("what is your physics grade?"))
# Chemistry = float(input("What is your chemistry grade?"))
# Biology = float(input("What is your biology grade?"))
# Geography = float(input("What is your geography grade?"))
# Sum = float(Math + Physics + Chemistry + Biology + Geography)

# Mean = float(Sum/5)

# print("Hello,{name},your average grade in the 5 subjects is {grade} %.".format( name=Name, grade=Mean))

# Assignment
# Strings
# 1. Write a Python Program that prints the reversed version of a string
String1 = "My name is Andrew"
print(String1[::-1])

# 2. Write a Python program that prints the length of a string s
print(len(String1))

# 3. Write a Python program that prints the character at index i in the string
print(String1[8])

# 4. Write a Python program that prints the first and last three characters of the string s as a single string.
# print(String1[0:3] + String1[14:17])
print(String1[0:3] + String1[-3:])

# 5.Write a Python program that prints the string s without the characters located at even indices.
print(String1[: :2])

# 6. Write a Python program that check if a string only contains numbers.
string2 = "Python is very usefull in 2022"
print(string2.isdigit())
# isdidit()-> If the string only contains numbers it returns true if not it returns false

# Write a Python program that prints the string s without the character at index n
def remove_ele(str, n): #-> defines our new function
      first_part = str[:n] #-> the start of the string upto the defined index
      last_part = str[n+1:] #-> the defined index +1 which means the defined index is skipped
      return first_part + last_part #-> put the two togther
print(remove_ele(string2, 0)) #Allows you to specify which index you want to exclude

# 8. Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
string3 = "Python is used in data science"
curr_char = string3[0]
new_char = "W"
print(string3.replace(curr_char,new_char))

# Lists
# 1. Write a Python program that multiplies all the items in a list by the value of the variable factor.
list1 = ["Python", "Java", "C#", "HTML", "Swift"]
print(list1*3)

# 2. Write a Python program that prints the elements of a list on the same line.
print(*list1)

# 3. Write a Python program that prints the largest and smallest values in a list
list2 = [11, 44, 55, 99, 77, 22, 66, 33, 88]
print(max(*list2),min(*list2))

# 4. Write a Python program that checks if a list is empty or not.
list3 = []

def check_empty(list):
    if (len(list)) == 0:
        print("The list is empty")
    else:
        print("The list is not empty")
        
check_empty(list2)
check_empty(list3)

# 5. Write a Python program that prints the elements of a list followed their corresponding indices
list4 = ["CSS", "SQL", "GO", "Kotlin", "Rust"]
print(list4[3] , list4.index("Kotlin"))
    


