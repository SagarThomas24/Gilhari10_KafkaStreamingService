import requests
import json


entities = [
    {"department_no": 1, "department_name": "Sales", "Nmuber_of_Employees": 0},
    {"department_no": 2, "department_name": "IT", "Nmuber_of_Employees": 0},
    {"department_no": 3, "department_name": "Finance", "Nmuber_of_Employees": 0},
    {"department_no": 4, "department_name": "Marketing", "Nmuber_of_Employees": 0},
    {"department_no": 5, "department_name": "HR", "Nmuber_of_Employees": 0}
]


data_to_send = json.dumps({"entity": entities})


url = "http://localhost:80/jdx/v1/Department/"


headers = {
    "Content-Type": "application/json"
}


response = requests.post(url, headers=headers, data=data_to_send)


if response.status_code >= 200 and response.status_code < 300:
    print("Data sent successfully")
else:
    print(f"Failed to send data. Status code: {response.status_code}, Response: {response.text}")