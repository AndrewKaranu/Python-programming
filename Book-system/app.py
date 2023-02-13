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
    name = input("Enter the new book title: ")
    author = input("Enter the books author: ")
    database.add_book(name, author)
        

def list_books():
    database.list_books()
    
def book_read():
    book_name = input("Enter the name of the book you would like to mark as read: ")
    database.mark_book_as_read(book_name)
    
def book_delete():
    book_name = input("Enter the name of the book you would like to delete ")
    database.delete_books(book_name)
    

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
        elif user_input == "l":
            list_books()
            
        elif user_input == 'r':
            book_read()
        elif user_input == 'd':
            book_delete()
        else:
            print("Invalid choice, please try again")
        user_input = input(USER_CHOICE)
    
    
    
menu()