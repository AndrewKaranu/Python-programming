import json

try: #Creates or updates the inventory.json to prevent the dictionary frombeing overwritten
    with open("books.json", "r") as f:
        books = json.load(f)
except FileNotFoundError:
     books = []

def save_inventory(): 
    with open("books.json", "w") as f:
        json.dump(books, f)
        
MENU_OPTIONS = "1. Add a new book [1] \n 2. Delete an existing book[2] \n 3. Mark a book as read or not read[3] \n 4. Print all books 5.Quit[5]"

def add_Book():
    book_title = input("Enter the new movies title: ")
    book_author = input("Enter the movies director: ")
    read_or_not = input("Enter the movies release year: ")
    
    books.append({
        "title": book_title,
        "director": book_author,
        "release year": read_or_not
    })

def delete_Book(book):
    if book in books:
        books =- book
        print("Removed {book} from inventory")

def mark_as_Read():
    pass

def menu():
    selection = input(MENU_OPTIONS)
    while selection != '5':
        if selection == '1':
            add_Book()
        elif selection == "2":
            del_book = input("Which bookwould you like to delete?")
            delete_Book(del_book)
            
        elif selection == '5':
            print(books)
        else:
            print("Invalid choice, please try again")
        selection = input(MENU_OPTIONS)
    save_inventory()
    
menu()