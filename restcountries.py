import requests

url = "https://restcountries.eu/rest/v2/all"

request = requests.get(url)

print(request.status_code)