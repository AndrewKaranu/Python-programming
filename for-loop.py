# Python Loops
# For loop
Vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]

for each_vendor in Vendors:
    print(each_vendor)
    print(each_vendor.upper())
    
my_string = "Cisco"

for letter in my_string:
    print(letter)
    print(letter * 2)
    print(letter * 3)
    
# For loops execute all the code for one element before moving to the next

my_range = range(0,10)


for i in my_range:
    print(i * 2)
    
# len(Vendors)
# range(5)
# print(list(range(5)))
# range(len(Vendors))

# Create a for loop that prints out each element of the vendors list by its index
for element_index in  range(len(Vendors)):
    print(element_index,Vendors[element_index])
    
for each_vendors, Vendors in enumerate(Vendors):
    print(f"elementin at index {each_vendors} is {Vendors}")
    
# enumerate->extracts indexes from their elements
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)
    
    
# What we did here is we passed the result of one function, len(), to anotherfunction, rnage(). The result is a range consistingof all the indexes in the vendors list. 
# We then assigned each index in the range to the element index temporary variable andexecuted a piece of code for each index. In translation we told python to check the length of the vednors list, then create a range using tha length as an argumnet forthe range() function.

# Finally, Python print out each element by its index
# vendors[0], vendors[1] and so on until the list is exhausted

# Write a python program that prints out all the negative odd numbers between the range of 0-51
neg_num = list(range(-51,0))
list1 = []
for num in neg_num:
    if num%2 != 0 and num<1:
        print(num)
        list1.append(num)
                   
print(list1)
print(max(list1))
print(min(list1))
    