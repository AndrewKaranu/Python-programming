# a while loop executes a piece of code as long as a user defined condition isevaluated as true. If the specified conditon does not change menaing it doesnt become flase, the the while loop will continue running forver and we end upwith an infinte loop
# When the condition becomes false, python continues to execute the code following the while loop
# To create a while loop you have to type in the while keyword, followed by the condition you want to evaluate and then a colon.
# Below you will specify the code to be execute as long as the condition is evaluated as true
 

x = 1 
while x <= 10:
    print(x)
    x = x + 1
    
# Another way to work with while loops is by using an expression which always evaluates as true, in order tomake python do something over and over again until you tell it to quit
# A great example would be an interactive menu where the user can select the value and execute a peice of code then retun to the main menu an so on. The wya to do this is by simply using while True, which makes sure that the expression is always evaluated as true.
# The syntax would be:
# while True:
#       do something

# Nested loops
# Lets assume we have two lists and we want to multiply each element of the first list by each element of the second list
# For this we would iterate over both lists at the same time,take each element into account, do the multiplcations and return the results
# list1 = [4, 5, 6]
# list2 = [10, 20, 30]

# for x in list1:
#     for y in list2:
#         print(x*y)


# Write a python prgram that generates the mathematical times table using user import


user_input = int(input("What number woud you like to see:"))
time_t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for x in time_t:
    print(f"{x} X {user_input}={x*user_input}")
    

time_t2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]       

for x in time_t:
    for y in time_t2:
      print(f"{x} X {y}={x*y}")
      print("----------------------------------------")  

    