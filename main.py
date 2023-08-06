import requests

APPLICATION_ID = "78fd8809"
API_KEY = "d3af93b3e39860bba3e2bd1100497b8d"

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"


PARAMS = {
    "query":"ran 3 miles",
    "gender": "male",
    "weight_kg": 75,
    "height_cm": 177,
    "age": 20
}


HEADERS = {
    "x-app-id": APPLICATION_ID, 
    "x-app-key": API_KEY
}


response = requests.post(url=EXERCISE_URL, json=PARAMS, headers=HEADERS)
print(response.json())

