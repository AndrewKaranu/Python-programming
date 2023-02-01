# Tuples-> immutable lists(their content cant be modified after creation)
my_tuple = ()
# print(my_tuple, type(my_tuple))

# tuple1 = (9) #-> this is an integer
# tuple2 = (9,) #->this is a tuple
# print(tuple1 == tuple2)

# print(type(tuple1) == type(tuple2))



my_tuple = (1, 2, 3, 4, 5)
# print(my_tuple[6])
# print(my_tuple[5]) ->both out of range


print(my_tuple[-2])
print(my_tuple[-1])
print(my_tuple[-0])

# since tuples are immutable, you cannot add or modify a tuple
# my_tuple[1] = 10
# print(my_tuple)-> gives a type error as tuples do not support item assignment

# del my_tuple[1]
# print(my_tuple)-> gives a type error as tuples do not support item deletion

# Variable assignment
tuple1 = ("Cisco", "2600", "12.4")
(vendor, model, ios) = tuple1
# (vendor, model, ios) = ("Cisco", "2600", "12.4") -> same as the above
print(model)
print(vendor)
print(ios)

# Tuple methods
tuple2 = (1, 2, 3, 4)
# len()
# Min()
# Max()
# Concatenate-> +
# Multiplication-> *
# Slicing->

# print(tuple2[0:2])
# [1:]
# [-3:]
# print(tuple2[::2])

# Membership-> in & not in

# del -> deletes the whole tuple
# del tuple2