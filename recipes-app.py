import requests

app_id = "514c0999" #->app id from the api website
app_key = "9a72596883830e9f3826dc7137c3e698" #->app key from the api website

Recipe = input("Enter recipe to search: ") #-> Gets user input on what recipe you wnat to get infromation on

url = "https://api.edamam.com/api/recipes/v2?type=public&q={recipe}&app_id=514c0999&app_key=9a72596883830e9f3826dc7137c3e698%09".format(recipe=Recipe)
# -> The link is used to access the information on the recipes. By changing the key word in the link with the use input we can search for all recipes with on link
recipe_request = requests.get(url)  #->request information from the link

print(recipe_request.status_code) #->prints the status code to determine if the api is working

# print(recipe_request.json())

recipes = recipe_request.json() #->Request the information of the recipes in json form
print(recipes["count"])
print(recipes["hits"][0]["recipe"]["label"])

