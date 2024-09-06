import requests
from datetime import datetime

# Info is hidden for security
APP_ID = "YOUR ID"
API_KEY = "YOUR KEY"
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# These should be ints
WEIGHT = "YOUR WEIGHT"
HEIGHT = "YOUR HEIGHT"
AGE = "YOUR AGE"

sheety_endpoint = "ENDPOINT"
USER = "YOUR_USER"
PASSWORD = "YOUR_PASS"

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
  }

nutri_parameters = {
    "query": input("Tell me which exercises you did today!: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
nutri_response = requests.post(url=nutritionix_endpoint, json=nutri_parameters, headers=headers)
print(nutri_response.text)
data = nutri_response.json()

current = datetime.now()
date = datetime.strftime(current, f"%d/%m/%Y")
time = datetime.strftime(current, f"%X")

for exercise in data["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    sheety_response = requests.post(url=sheety_endpoint,
                                    json=sheety_parameters,
                                    auth=(USER, PASSWORD)
                                    )
    print(sheety_response.text)
