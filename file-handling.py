# files
# open() -> used for openning files
        #-> it takes two parameters which are "file_name" and the "mode" in which the file is to be opened
# We have several modes for opeing a file with:
# 1. read mode-> 'r': reading a file
# 2. write mode-> 'w': writing to a file
# 3. append mode-> 'a': appending to a file without overwriting the content
# 4. delete-> 'x': deleting a file

# Write mode->
# append mode-It adds onto the existing data
# file = open("people.txt","a")
# file_content = file.write("Python Programming\n")
# file.close()

# write mode- It overwrites the existing data
# file = open("my_file.txt", "w")
# user_name = "Andrew Karanu"
# file.write(user_name)
# file.close()

# Both write modes create the file of it doesnt exists

# Read mode->
# file = open("people.txt", "r")
# file_contents = file.read()
# file.close()
# print(file_contents)

# Using context managers to open files
# with open("people.txt", "r") as file:
#     fil_contents = file.read()
#     print(fil_contents)
    

# Using context managers to write to files
# with open("my_file.txt", "a") as file:
#     user_name = "Karanu Andrew"
#     fil_contents = file.write(user_name)
#     print(fil_contents)


# # Deleting a file
# import os, sys
# os.remove("my_file.txt")

# import datetime
# # print(datetime.date.today()) ->prints the current date
# omw_date = datetime.datetime(2023, 2, 10) #->prints a day a given datefalls on
# print(omw_date.strftime("%a"))
# print(omw_date.strftime("%d"))
# print(omw_date.strftime("%b"))

# 1. Write a short python script which queries the user for input (infinite loop with exit posibility) and writes input to a file
# 2.Add another option to your user interface (UI): The user should be able to output the data stored in the file in the terminal
# 3. Store the user input in a list (instead of directly adding it to the file) and write that list to the file using json and pickle
# 4. Adjust the logic to work with pickled/jsoned file

# while True:
#     input_quest = "What would you like to write?"
#     file_input = input(input_quest)
    
#     with open("my_file.txt", "a") as file:
#         user_input = file_input
#         fil_contents = file.write(user_input + "\n")
#     with open("my_file.txt", "r") as file:
#         fill_contents = file.read()
#         print(fill_contents)
        
    
#     back = input("Do you wish to give another input? (Y) or (N): ")
#     if back.lower() == "y":
#             continue
#     else:
#         break 
    

        
# running = True
# while running:
#     print("Please Choose from the Menu?")
#     print("1. Add input")
#     print("2. Output data")
#     print("d. Delete")
#     print("q. Quit")
#     user_choice = input("Enter your choice: ")
#     if user_choice == "1":
#         data_To_Store = input("Please provide your input: ")
#         with open("sample.txt", "a") as f:
#             f.write(data_To_Store)
#             # f.write("\n")
#     elif user_choice == "2":
#         with open("sample.txt", "r") as f:
#             content = f.readlines()
#             print(content)
#     elif user_choice == "d":
#         import os, sys
#         file_to_delete = input(str("Which file would you like to delete? "))
#         os.remove(file_to_delete)
#     elif user_choice == "q":
#         running = False
    
    

# import pickle,json
# # json.loads -> Json to python
# # json.dumps -> Python to Json
import json
User_input_list = []
running = True
while running:
    print("Please Choose from the Menu?")
    print("1. Add input")
    print("2. Output data")
    print("d. Delete")
    print("q. Quit")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        data_To_Store = input("Please provide your input: ")
        User_input_list.append(data_To_Store)
        with open("sample.txt", "w") as f:
            for content in User_input_list:
                f.write(json.dumps(User_input_list))
    elif user_choice == "2":
        with open("sample.txt", "r") as f:
            file_contents = json.loads(f.read())
            for line in file_contents:
                print(file_contents)
    elif user_choice == "d":
        import os, sys
        file_to_delete = input(str("Which file would you like to delete? "))
        os.remove(file_to_delete)
    elif user_choice == "q":
        running = False








