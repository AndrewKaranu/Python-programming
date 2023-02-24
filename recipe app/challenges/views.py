from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
import requests

app_id = "514c0999" #->app id from the api website
app_key = "9a72596883830e9f3826dc7137c3e698" #->app key from the api website

Recipe = input("Enter recipe to search: ") #-> Gets user input on what recipe you wnat to get infromation on

url = "https://api.edamam.com/api/recipes/v2?type=public&q={recipe}&app_id=514c0999&app_key=9a72596883830e9f3826dc7137c3e698%09".format(recipe=Recipe)
# -> The link is used to access the information on the recipes. By changing the key word in the link with the use input we can search for all recipes with on link
recipe_request = requests.get(url)  #->request information from the link

# print(recipe_request.status_code) #->prints the status code to determine if the api is working

# print(recipe_request.json())

recipes = recipe_request.json() #->Request the information of the recipes in json form
# print(recipes["count"])


# Create your views here.
monthly_challenges = {
    "january":"Eat no meat the entire month",
    "february":"Excercise every day of the month",
    "march":"Read a book every week",
    "april":"Drink 2 litres of water every day",
    "may":"Drink 2 litres of water every day",
    "june":"Drink 2 litres of water every day",
    "july":"Drink 2 litres of water every day",
    "august":"Drink 2 litres of water every day",
    "september":"Drink 2 litres of water every day",
    "october":"Drink 2 litres of water every day",
    "november":"Drink 2 litres of water every day",
    "december": None,
    
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html",{
        "months":months
    })

def monthly_challenge_by_number(request, month):
    try:
        months = list(monthly_challenges.keys())
        redirect_month = months[month - 1]
        redirect_path = reverse("month_challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
        
    # "http://127.0.0.1:8000/redirect_month"
    except:
        return HttpResponseNotFound("Invalid Month")
    
    
def find_recipe(request):
    recipe_name = (recipes["hits"][0]["recipe"]["label"])
    ingredients = (recipes["hits"][0]["recipe"]["ingredientLines"])
    return render(request, "recipes/index.html",{
        "recipe":"pancake",
        "ingredients": ingredients})

# def monthly_challenge_by_number(request, month):
#     try:
#         months = list(monthly_challenges.keys())
#         redirect_month = months[month - 1]
#         # redirect_path = reverse()
#         return HttpResponseRedirect("/challenges/" + redirect_month)
#     # "http://127.0.0.1:8000/redirect_month"
#     except:
#         return HttpResponseNotFound("Invalid Month")
    
# months = list(monthly_challenges.keys())


    
def monthly_challenge(request, month):
    challenge_text = monthly_challenges[month]
    return render(request, "challenges/challenge.html", {
        "challenge_text": challenge_text,
        "month": month,
    })


        


