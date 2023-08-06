import requests
from datetime import datetime as dt 

GENDER = "male"
WEIGHT_KG = 75
HEIGHT_CM = 177
AGE = 20

APPLICATION_ID = "78fd8809"
API_KEY = "d3af93b3e39860bba3e2bd1100497b8d"

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/ab0faa02bd1bfe5baf97a93bd0872a6d/calorieTrackingUsingNlp/workouts"

exercise_input = input("Congratulations on being active! Which exercises did you do?")


PARAMS = {
    "query":exercise_input,
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
data = response.json()

now_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")


for exercises in data["exercises"]:
    sheet_params = {
        "workout": {
            "date": now_date,
            "time": now_time,
            "exercise": exercises["name"].title(),
            "duration": exercises["duration_min"],
            "calories": exercises["nf_calories"]
        }
    }

    exercise_response = requests.post(url=SHEET_URL, json=sheet_params)
    print(exercise_response.text)