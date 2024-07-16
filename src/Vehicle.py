import requests
import json

# Corrected data list
entities = [
    {"Vehicle_id": 1, "Type": "Car", "No_of_vehicles": 10},
    {"Vehicle_id": 2, "Type": "Scooter", "No_of_vehicles": 10},
    {"Vehicle_id": 3, "Type": "Bike", "No_of_vehicles": 10},
    {"Vehicle_id": 4, "Type": "Truck", "No_of_vehicles": 10},
    {"Vehicle_id": 5, "Type": "Bus", "No_of_vehicles": 10}
]
data_to_send = json.dumps({"entity": entities})

url = "http://localhost:88/jdx/v1/Vehicle/"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, data=data_to_send)

# Check the response
if response.status_code >= 200 and response.status_code < 300:
    print("Data sent successfully")
else:
    print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")
