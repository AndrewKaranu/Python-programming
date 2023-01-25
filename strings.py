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
# print("2" + 2) -> TypeError: can only concatenate str (not "int") to str
# print("2" + "2") -> give 22 as a string not integer
# print(2 + 2) -> gives 4 as an integer

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
print(string3.replace(" ", ""))

# Create a variable and store your name in small letter. chage your name to have the first letter in caps
# 10. Capitalize
string5 = "andrew"
print(string5.capitalize())

# 11. split() -> splits a string into substring and returns a list
string6 = "cissco,juniper,hp,avaya,nortel"

print(string6)
print(string6)
print(len(string6))
string6 = string6.split(",")
print(string6)
print(len(string6))

# 12. join() -> Allows you to separate characters in a string with your character of choice
string7 = "Cisco Switch"
print("_".join(string7))
print("#".join(string6))

# 13. string slicing -> allowsyou to cut a certain specified portion of a string

string8 = "0 E2 10.110.8.9 [160/5] via 10.119.254.6, 0:01:00 Ethernet2"
print(string8[5:15])
print(string8.index("1"))
print(string8.find("t2"))
print(len(string8))
print(string8[5:])  #if you dont specify the last character it goes to the end
print(string8[:11]) #if you dont specify the first character it starts from the first character in the string
print(string8[:])  #if you dont specify anything it covers the whole string
print(string8[:-48]) 

print(string8[::2]) #This prints every other character in the string
# Print hre2
print(string8[52:59:2])

print(string8[::2])
sliced = string8[::2]

print(sliced[-4:])
# Change hre2 into CRE
sliced2 = sliced[-4:-1]
   
print(sliced2.replace("h", "C").upper())
Sliced3 = sliced2.replace("h", "C").upper()
# Change CRE into C.R.E

print(".".join(Sliced3))

print(".".join(sliced2.replace("h", "C").upper())) #All the code in one line

# 14. Printing a string in reverse order usimg slicing and step
# By setting the step to -1 we can reverse the string

print(string8[::-1])
