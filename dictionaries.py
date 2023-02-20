# Dictionary-> set of key-value pairs  separated by comma(s)

dict1 = {}
# print(dict1, type(dict1)) 

 

# Finding a specific value within a string in a value of a key
dict2 = {"Vendor": "cisco", "Model": "2600", "IOS": [12.3, 14.0, 15.6,16.1],"Ports": "4"}
print(dict2["IOS"][2])

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

# Another way to generate dictionaries
dict3 = dict(a = list(range(1,11)), b = list(range(12,22)))
print(dict3)
