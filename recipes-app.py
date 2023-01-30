import requests

app_id = "514c0999"
app_key = "9a72596883830e9f3826dc7137c3e698"

Recipe = input("Enter recipe to search: ")

url = "https://api.edamam.com/api/recipes/v2?type=public&q={recipe}&app_id=514c0999&app_key=9a72596883830e9f3826dc7137c3e698%09".format(recipe=Recipe)

recipe_request = requests.get(url)

print(recipe_request.status_code)

# print(recipe_request.json())

recipes = recipe_request.json()
print(recipes["count"])
print(recipes["hits"][0]["recipe"]["label"])

