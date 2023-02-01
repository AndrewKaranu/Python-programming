# Ranges
R = range(10)
print(R)
print(type(R))

# List method/constructor-> turns the range object into a list
R = list(range(10))
print(R)

# [O, 2, 4, 8]
print(R[::2])

# -12, -10, -8 
list1 = list(range(-12,-1))
print(list1[::2])

# print(list(range(-12,-1)[::2]))

# r2 = list(range(-12,0,2))
# print(r2)
