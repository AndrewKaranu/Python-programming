# SETS-> Unordered collection of unique elements
# 
List1 = [1, 2, 3, 4, 5, 2,3]
print(set(List1)) #-> prints {1, 2, 3, 4, 5} and proves that sets do not allow duplicates

# Making a set by passing a raw sequence into the set function
set1 = set([11, 12, 13, 14, 15, 15, 15, 11])
print(set1, type(set1))

# Making a set using curly braces {}
set2 = {11, 12, 13, 14, 15, 15, 15, 11}
print(set2, type(set2))

# len() -> finds the number of elements in the set
print(len(set2))

# Finding whether an element is or isnt in a set with in and not in 
print(11 in set2)
print(17 in set2)
print(16 not in set2)
print(12 not in set2)

# .add-> used to add elements to a set
set2.add(16)
set2.add(20)
set2.add(2)
set2.add(100)
set2.add(40)
print(set2)

# remove -> removing an element from a set
set2.remove(15)
print(set2)

set3 = {1, 2, 3, 4}
set4 = {3, 5, 8}

# Intersection() ->finds the common elements in two sets
# print(set3.intersection(set4))

# # Difference() -> checks which elements are unique to a set
# print(set3.difference(set4))
# print(set4.difference(set3))

# Union() -> unifys two sets while getting rid of duplicates
# print(set3.union(set4))

# pop() -> removes a random element from a set
# print(set3.pop())
# print(set3)
# you can also sepcify what element you want to remove by specifying it in the pop() function
# set4.pop()
# print(set4)
# 
# update() -> Adds one set to another
# print(set3.update(set4))

# clear()-> clears the set
print(set3.clear())

set5 = {}
print(set5.clear(), type(set5))

