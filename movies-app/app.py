import json

try: #Creates or updates the inventory.json to prevent the dictionary frombeing overwritten
    with open("movies.json", "r") as f:
        movies = json.load(f)
except FileNotFoundError:
     movies = []

def save_inventory(): 
    with open("movies.json", "w") as f:
        json.dump(movies, f)
# Creat an empty list tosote our movies


# Displaye the menu to the user
MENU_OPTIONS = "\nEnter \n- 'a' to add a movie \n- 'l' to see your movies \n- 'f' to find a movie by its title  \n- 'q' to quit \nEnter choice: "

#  Create a funtion to creat a movie
def add_Movie():
    movie_title = input("Enter the new movies title: ")
    movie_director = input("Enter the movies director: ")
    movie_releaseyear = input("Enter the movies release year: ")
    
    # Add the moviedictionary into our list
    movies.append({
        "title": movie_title,
        "director": movie_director,
        "release year": movie_releaseyear
    })

# Helper function for printing the movie in a nice format
def print_movie(movie):
    print(f"{movie['title']}, directed by {movie['director']} and released in {movie['release year']} ")
    
# Create a funtion to list all the movies in ourcollection
def show_movies():
    for movie in movies:
        print_movie(movie)

def find_movie():
    title = input("Enter the movie title: ")
    for movie in movies:
        if movie['title'] == title:
        # if title in movie['title'].lower():
            print_movie(movie)
    if movie['title'] != title:
                print(f"The movie {title} can not be found in the directory")

        
def menu():
    selection = input(MENU_OPTIONS)

    while selection != 'q':
        if selection == 'a':
            add_Movie()
        elif selection == "l":
            show_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Invalid choice, please try again")
        selection = input(MENU_OPTIONS)
    save_inventory()
# Call the menu method
menu()
