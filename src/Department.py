import requests
import json

# Corrected data list
entities = [
    {"dno": 1, "d_name": "Sales", "Nmuber_of_Employees": 0},
    {"dno": 2, "d_name": "IT", "Nmuber_of_Employees": 0},
    {"dno": 3, "d_name": "Finance", "Nmuber_of_Employees": 0},
    {"dno": 4, "d_name": "Marketing", "Nmuber_of_Employees": 0},
    {"dno": 5, "d_name": "HR", "Nmuber_of_Employees": 0}
]

# Convert the list of entities to the required JSON structure
data_to_send = json.dumps({"entity": entities})

# Specify the URL
url = "http://localhost:80/jdx/v1/Department/"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Send the data
response = requests.post(url, headers=headers, data=data_to_send)

# Check the response
if response.status_code >= 200 and response.status_code < 300:
    print("Data sent successfully")
else:
    print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")