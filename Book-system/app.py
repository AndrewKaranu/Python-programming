from utils import database
USER_CHOICE = """"
Enter: 
- 'a' to add new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Enter choice: """


def add_Book():
    name = input("Enter the new movies title: ")
    author = input("Enter the movies director: ")
    database.add_book(name, author)
        

def lis_books():
    pass

# A function that asks the user for book name and changes it to read in our list
def prompt_read_book():
    pass

# Deletes a book when given name
def delete_books():
    pass

# The menu
def menu():
    user_input = input(USER_CHOICE)
    #dealwith the users input choice
    while user_input != 'q':
        if user_input == 'a':
           add_Book()
        elif selection == "2":
            pass
            
        elif selection == '5':
            pass
        else:
            print("Invalid choice, please try again")
        selection = input(USER_CHOICE)
    
    
menu()