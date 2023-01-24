# strings

paragraph = """Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
It has survived not only five centuries, but also the leap into electronic typesetting, 
remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset 
sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""

print(paragraph)

name = "Andrew"
user_name = "Andrew"

#print TYPE
print(type(paragraph))
print(type(name))
print(type(user_name))


print(type(user_name), user_name)

#You cant add a string and integer
# print("2" + 2)

# INDEXING

string1 = "Cisco Router"

# Accessing first character in string
print(string1[0])

# Accessing the third element in the string 
print(string1[2])

# Accessing the space character in the string 
print(string1[5])

# Negative indexing- accessing the last character in the string
print(string1[-1])

# Negative indexing- accessing the first character in the word Router
print(string1[-6])

# Counting the number of character in a string with Len() function
len(string1)
print(len(string1))
print(len(paragraph))

# Accessing an element using an invalid index
# print(string1[100]) #retruns an index error due to the index being out of range

# String Methods
string2 = "Cisco Switch"

# 1. index() -> returns the index of given character in a string (first occurence)-it is also case 
print(string2.index("c"))
print(string2.index("C"))
print(string2.index("s"))
print(string2.index("S"))

# 2. Count() -> returns the number of time an element appears in a string
print(string2.count("i")) #returns 2
print(string2.count(" ")) #returns 1

# 3.  Find() -> searches for a sequence of characters and reurns the index where the string starts
print(string2.find("sco"))
print(string2.find("tch"))
print(string2.find("Swi"))
print(string2.find("xyz"))

# sub = "xyz"

# if string2.find(sub)==-1
# print(f'"{sub} was not matched')

# 4. lower() -> transforms a string into lower case
print(string2.lower())

# 5. upper() -> transforms a string into upper case
print(string2.upper())

# Upper() and Lower() dont change the initial string. This shows that they are immutable

# 6. startswith()
print(string2.startswith("S")) #returns true
print(string2.startswith("x")) #returns false
# 7. endswith()
print(string2.endswith("h")) #returns true
print(string2.endswith("z")) #returns false

#  8. strip() -> eliminates all white from the start and end of a string
string3 = "    Cisco Switch   "
print(string3)
print(string3.strip())

print(len(string3))
print(len(string3.strip()))

string4 = "###Cisco Router###"
print(string4.strip("#"))

# 9. replace() -> replaces a specified character with a given character
print(string3.replace(" ", " "))