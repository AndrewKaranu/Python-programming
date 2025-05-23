# # list1 = []
# # print(type(list1), list1, len(list1))
# list1 = ["Cisco", "Juniper", "Avaya", 10, 10.5, -11]
# print(list1)

# # Lets find the number of elements in this list
# print(len(list1))
# # print out Cisco
# print(list1[0])
# # print out -11
# print(list1[-1])

# # Proving that lists are mutable
# # method 1: indexing and replaceing
# list1[3] = "HP"
# print(list1)

# List methods
# min() -> minimum value in list
# list2 = [-11,2 ,12]
# print(min(list2))

# # max() -> maximum value in list
# print(max(list2))

# list3 = ["a", "b", "c", "You", "@"] #->Uses ASCII code values to find what letter or symbol is max 
# # For words like YOU it looks at the first letter
# print(max(list3))

# Using strings and integers with max and min
# list4 = ["a", "b", "c", 1 , 2, 3]
# print(max(list4))
# You get a type error as you cant compare between integers and strings

# list4 = ["yours", "yield" , "yen"]
# print(max(list5))

# Appending an element to a list -> append()
list4 = ["a", "b", "c", "You", "@"]
# # list4.append(100)
# list4.append(50)
# list4.append("me")
# print(list4)

# Removing an element from a list
# # 1. Using del command
# del list4[-1]
# print(list4)

# # 2. Uisng pop() -> Uses index of element you want to remove
# list4.pop(0)
# print(list4)

# 3. uSING REMOvE->deleting the value by specifying 
# list5.remove("")
# print(list5)

# Appending a list to another list
# list5 = []
# list4.extend(list5)
# print(list5)

#  find out the index of an element in  a list ->
# lis

# print(list4.index("c"))

# # count occurence of an element in a list

# list4.append(32)
# list4.append(32)
# list4.append(32)
# print(list4.count(32))

# # Sort()->used to arrange list in ascending order
list6 = [3, 55, 1, 54, 65, 10, 32, 9]
# list6.sort()
# print(list6)

# # reverse()-> sorts a list in descending order
# list6.reverse()
# print(list6)

# sorted()-> creates a new list in memory
sorted(list6)
print(list6)
print(sorted(list6, reverse=True))

# Concatenate/repeat
print(list6 + list6)
print(list6 * 3)

# List slicing-> extracts various parts of a sequence
List7 = [1, 2, 3, "a", "b", "c"]
#extracts the first three elements in List7
print(List7[0:3]) 
print(List7[-6:-3])
print(List7[:3])
print(List7[0:-3])
# output -> [3, "a", "b"]
print(List7[2:5])
print(List7[-4:-1])
print(List7[2:-1])

# ["a", "b", "c"] using negative indexing
print(List7[-3:])
# get the entire list
print(List7[0:])
print(List7[-6:])
print(List7[:])

# [1, 3, "b"]
print(List7[::2])
# ['c', 'b', 'a', 3, 2, 1]
print(List7[::-1])
# Create a list of numbers 0-12, create a slice that has [0, 2, 4, 6, 8, 10, 12]
list8 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list8[::2])
# Create a list of alphabet letters -> ["b", "d", "f", "h", "j", "l"]
list8 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
print(list8[1::2])

# Generates letters as a list
from string import ascii_lowercase
letters = ascii_lowercase
print(list(letters))
print(list(letters)[0:12])
# Generates numbers
print(list(range(1,12)))

# SETS
