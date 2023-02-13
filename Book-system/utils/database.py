# Create an empty list to store our book
# books = []


# def add_book(name, author):
#     books.append({
#         "name":name,
#         "author":author,
#         "read": False
#     })
#     print(f"{name} by {author} was succesfully added")
    
# # Create a function that displays all the books to the user
# def list_books():
#     print(books)

# print(books)
import json

def load_books():
    global books
    try:
        with open('books.json', 'r') as f:
            books = json.load(f)
    except FileNotFoundError:
        books = []
        
def save_books():
    with open('books.json', 'w') as f:
        json.dump(books, f)

        
# Load the books from the file
load_books()

def add_book(name, author):
    books.append({
        "name":name,
        "author":author,
        "read": False
    })
    save_books()
    print(f"{name} by {author} was successfully added")

# Create a function that displays all the books to the user
def list_books():
    for book in books:
        name = book['name']
        author = book['author']
        read = book['read']
        read_status = 'Read' if read else 'Not read'
        print(f"{name} by {author} ({read_status})")

def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] == True
            print(f"{name} has been marked as read")
            save_books()
            return
    print(f"Could not find book with name {name}.")
    
def delete_books(name):
    for book in books:
        if book["name"] == name:
            books.remove(book)
            print(f"{name} has been deleted.")
            save_books()
            return
    print(f"Could not find book with name {name}.")