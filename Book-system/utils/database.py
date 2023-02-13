# Create an empty list to store our book
books = []

# create a function that adds a bookto our list
def add_book(name, author):
    books.append({
        "name":name,
        "author":author,
        "read": False
    })
    print(f"{name} by {author} was succesfully added")
    
# Create a function that displays all the books to the user
