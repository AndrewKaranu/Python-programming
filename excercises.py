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
# String1 = "My name is Andrew"
# print(String1[::-1])

# # 2. Write a Python program that prints the length of a string s
# print(len(String1))

# # 3. Write a Python program that prints the character at index i in the string
# print(String1[8])

# # 4. Write a Python program that prints the first and last three characters of the string s as a single string.
# # print(String1[0:3] + String1[14:17])
# print(String1[0:3] + String1[-3:])

# # 5.Write a Python program that prints the string s without the characters located at even indices.
# print(String1[: :2])

# # 6. Write a Python program that check if a string only contains numbers.
# string2 = "Python is very usefull in 2022"
# print(string2.isdigit())
# # isdidit()-> If the string only contains numbers it returns true if not it returns false

# # Write a Python program that prints the string s without the character at index n
# def remove_ele(str, n): #-> defines our new function
#       first_part = str[:n] #-> the start of the string upto the defined index
#       last_part = str[n+1:] #-> the defined index +1 which means the defined index is skipped
#       return first_part + last_part #-> put the two togther
# print(remove_ele(string2, 0)) #Allows you to specify which index you want to exclude

# # 8. Write a Python program that prints the string s with the character curr_char replaced by the character new_char.
# string3 = "Python is used in data science"
# curr_char = string3[0]
# new_char = "W"
# print(string3.replace(curr_char,new_char))

# # Lists
# # 1. Write a Python program that multiplies all the items in a list by the value of the variable factor.
# list1 = ["Python", "Java", "C#", "HTML", "Swift"]
# print(list1*3)

# # 2. Write a Python program that prints the elements of a list on the same line.
# print(*list1)

# # 3. Write a Python program that prints the largest and smallest values in a list
# list2 = [11, 44, 55, 99, 77, 22, 66, 33, 88]
# print(max(*list2),min(*list2))

# # 4. Write a Python program that checks if a list is empty or not.
# list3 = []

# def check_empty(list):
#     if (len(list)) == 0:
#         print("The list is empty")
#     else:
#         print("The list is not empty")
        
# check_empty(list2)
# check_empty(list3)

# # 5. Write a Python program that prints the elements of a list followed their corresponding indices
# list4 = ["CSS", "SQL", "GO", "Kotlin", "Rust"]
# print(list4[3] , list4.index("Kotlin"))
    

# Name = input("what is your name?")
# Math = float(input("What is your math grade?"))
# Physics = float(input("what is your physics grade?"))
# Chemistry = float(input("What is your chemistry grade?"))
# Biology = float(input("What is your biology grade?"))
# Geography = float(input("What is your geography grade?"))
# Sum = float(Math + Physics + Chemistry + Biology + Geography)

# Grade_list = [Math, Physics, Chemistry, Biology, Geography]
# print(Grade_list)

# Mean = sum(Grade_list)/len(Grade_list)

# print("Hello,{name},your average grade in the 5 subjects is {grade} %.".format( name=Name, grade=round(Mean,1)))

# automatically adding subjects to list
# Create empty list
# subjects = []

# store the marks in a list
# subjects.append(Math)
# subjects.append(Physics)
# subjects.append(Chemistry)
# subjects.append(Biology)
# subjects.append(Geography)

# print(subjects)

# Create a dictionary

# dict1 = {"a":list(range(1,11)), "b":list(range(11,21)), "c":list(range(21,31))}
# print(dict1)

# # dict = {letter: list(range((ord(letter) - 96) * 10 + 1, (ord(letter) - 96) * 10 + 11)) for letter in 'abc'}
# # print(dict)

# # print out:
# # a has [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # b has [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# # c has [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# dict2 = {"a has":list(range(1,11)), "b has":list(range(11,21)), "c has":list(range(21,31))}
# print("a has", dict2["a has"])
# print("b has", dict2["b has"])
# print("c has", dict2["c has"])

# for key, value in dict2.items():
#     print(key, value)

# #Print out 13
# print(dict2["b has"][2]) 

# For loop 
# Write a python program that prints out all the negative odd numbers between the range of 0-51

# Create a function to collect user name
# Create a function to collect user age
# Create a function to claculate age in seconds
# Create a function to print out the age in seconds


# Create a program that gets two numbers from the user and then checks if the sum is even or odd. Improve the prgram to also check if the numbers themselves are odd or even

# def even_odd():
#     x = int(input("First Number?"))
#     if x % 2 == 0:
#      print(f"{x} is even")
#     elif x % 2 > 0:
#         print(f"{x} is odd")
#     y = int(input("Second Number?"))
#     if y % 2 == 0:
#      print(f"{y} is even")
#     elif y % 2 > 0:
#         print(f"{y} is odd")
#     sum = x+y
#     if sum % 2 == 0:
#      print(f"sum of {x} and {y} is even")
#     elif sum % 2 > 0:
#         print(f"sum of {x} and {y} is odd")


# One complete statement

# def even_odd():
#     x = int(input("First Number?"))
#     if x % 2 == 0:
#      status = (f"{x} which is even")
#     elif x % 2 > 0:
#      status = (f"{x} which is odd")
#     y = int(input("Second Number?"))
#     if y % 2 == 0:
#      status2 = (f"{y} which is even")
#     elif y % 2 > 0:
#      status2 = (f"{y} which is odd")
#     sum = x+y
#     if sum % 2 == 0:
#      status3 = (f"is even")
#     elif sum % 2 > 0:
#      status3 = (f"is odd")
#     print(f"The sum of {status} and {status2} is {sum} which {status3}.")
    
# even_odd()
    
    
        

    
# 2nd method with multiple functions
      
# def checkIfOddorEven(num):
#     if num % 2 == 0:
#         status = (f"{num} which is even")
#     elif num % 2 > 0:
#         status = (f"{num} which is odd")  
#     return status

# def checkIfSumisOddorEven(sum):
#     if sum % 2 == 0:
#         stutus = (f"{sum} which is even")
#     elif sum % 2 > 0:
#         status = (f"{sum} which is odd") 
#     return status

# def calculateSumOfTwoNumbers():
#     num1 = int(input("First Number?"))
#     num2 = int(input("Second Number?"))
#     sum = num1 + num2
#     num1_status = checkIfOddorEven(num1)
#     num2_status = checkIfOddorEven(num2)
#     return[sum, num1_status, num2_status]
#     print(sum)


# def printResults():
#     sum = calculateSumOfTwoNumbers()
#     sum_status = checkIfSumisOddorEven(sum[0])
#     print(f"The sum of {sum[1]} and {sum[2]} is {sum_status}")
    
# printResults()


# string2 = ["123", "QWE", "CBA", "ABC"]
# string1 = "ABC"

# if len(string1) == 3 and check(string2)
#     print("yes")
# else:
#     print("no")


# Excercise on complex data types
# 1. Create a list of "person" dictionaries with a name age and a list of hobbies for each person. Fill in any data you want.

person = [
    {
        "name": "Andrew Karanu", 
        "age": 20,
        "hobbies": ["reading", "coding", "hiking"]
    },
    {
        "name": "Joseph Kimani", 
        "age": 33,
        "hobbies": ["reading", "coding", "hiking"]
    },
    {
        "name": "Lucy Nyawira", 
        "age": 27,
        "hobbies": ["reading", "coding", "hiking"]},
    {
        "name": "Joy Mungai", 
        "age": 19,
        "hobbies": ["reading", "coding", "hiking"]
    }
    ]

# 2. Use a list comprehension to convert this list of persons into a list of names (of the person)
names = [people["name"] for people in person]
print(names)

# 3. Use the list comprehension to check whether all persons are older than 20 years old
# age_above_20 = [people["age"] for people in person if people["age"] > 20]
# print(age_above_20)

# Printing false and true 
# new_list = []
# for people in person: 
#     if people["age"] > 20:
#         new_list.append("True")
#     else:
#         new_list.append("False")

# are_older = all(people["age"] > 20 for people in person) #->shows whether all values are true or false

# print(are_older)

# are_older = [people["age"] > 20 for people in person] #->shows true or false for each value
# print(are_older)
        
# print(new_list)


# 4. Copy the list such that you can safely edit the name of the first person(without changing the original list)
# person2 = person[:] ->doesnt work as the first list will still be affected
# print(person2)

# copied_person = [person.copy() for person in person]
# copied_person[2]["name"] = "Ian"
# print(copied_person)
# # 5. Unpack the persons of the original list into different variables and output these variables

# for person in copied_person :
#     name, age, hobbies = person["name"], person["age"], person["hobbies"]
#     print(f"Name: {name}, Age: {age}, Hobbies: {hobbies}")

# def add_to_parkone(animal, numberobserved):
#     if animal in animals_parkone:
#         animals_parkone[animal]["numberobserved"] += numberobserved
#     else:
#         animals_parkone[animal] = {"numberobserved": numberobserved}
#     print(f"Added {numberobserved} {animal}(s) to animals observed in park one.")

# def add_to_parktwo(animal, numberobserved):
#     if animal in animals_parktwo:
#         animals_parktwo[animal]["numberobserved"] += numberobserved
#     else:
#         animals_parktwo[animal] = {"numberobserved": numberobserved}
#     print(f"Added {numberobserved} {animal}(s) to animals observed in park one.")
# import pickle

# filename = "my_dict.pickle"

# try:
#     with open(filename, "rb") as f:
#         my_dict = pickle.load(f)
#         print("Loaded dictionary from file:", my_dict)
# except FileNotFoundError:
#     my_dict = {}
#     print("Created new empty dictionary")

# while True:
#     key = input("Enter a key: ")
#     value = input("Enter a value: ")
#     my_dict[key] = value
#     print("Added key-value pair:", key, "-", value)

#     another = input("Do you want to enter another key-value pair? (y/n) ")
#     if another.lower() != "y":
#         break

# with open(filename, "wb") as f:
#     pickle.dump(my_dict, f)
#     print("Saved dictionary to file:", my_dict)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}

# unique_keys = set(dict1.keys()) | set(dict2.keys()) - set(dict1.keys()) & set(dict2.keys())

# for key in unique_keys:
#     print(key)

# Create an empty outer dictionary
outer_dict = {}

# Prompt user for inner dictionary key-value pair
inner_key = input("Enter inner dictionary key: ")
inner_value = input("Enter inner dictionary value: ")

# Create inner dictionary
inner_dict = {inner_key: inner_value}

# Prompt user for outer dictionary key
outer_key = input("Enter outer dictionary key: ")

# Add or create key-value pair in outer dictionary
if outer_key in outer_dict:
    outer_dict[outer_key].update(inner_dict)
else:
    outer_dict[outer_key] = inner_dict

# Print the resulting outer dictionary
print(outer_dict)
