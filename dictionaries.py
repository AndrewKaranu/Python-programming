# Dictionary-> set of key-value pairs  separated by comma(s)

dict1 = {}
# print(dict1, type(dict1)) 

dict1 = {"Vendor": "cisco", "Model": "2600", "IOS": "12.4","Ports": "4"}

# Dictionary methods
# Indexing a value using its key
print(dict1["Vendor"])       
print(dict1["Model"])       
print(dict1["IOS"])       
print(dict1["Ports"])     

# Adding a new key-value pair  
# Insert-> RAM: 128
dict1["RAM"] = "128"
print(dict1)

# Making changes to the valuesof existing strings
dict1["IOS"] = "15.6"
print(dict1)

# Deleting a key-value pair
del dict1["Ports"]
print(dict1)

# len()-> find the number of key-value pairs in the dictionary
print(len(dict1))

# Veifying if a key is in a dictionary using in & out
print("IOS" in dict1)
print("Ports" not in dict1)

# keys() -> obtains a list of the keys in a dictionary
print(dict1.keys()) 
print(list(dict1.keys())) #->makes it into a proper list

# values()-> obtains a list of the values in a dictionary
print(dict1.values()) 
print(list(dict1.values()))

# items() -> obtains a list of tuples with each key & value in the dictionary in it
print(dict1.items()) 
print(list(dict1.items()))

# Python Conditionals if/elif/else