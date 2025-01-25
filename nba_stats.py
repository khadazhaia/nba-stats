import requests 
import json
import pandas as pd 


import requests

url = "https://api-nba-v1.p.rapidapi.com/players/statistics"

querystring = {"game":"8133"}

headers = {
    "x-rapidapi-key": "c36cdf577bmshd45ddc185bb8149p1e9651jsnfa4b198c7f76",
    "x-rapidapi-host": "api-nba-v1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

file_path = "data/json/data.json"

with open(file_path, "w") as file:
    json.dump(data, file, indent=4)