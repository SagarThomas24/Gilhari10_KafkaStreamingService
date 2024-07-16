import json
import requests
from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'myg',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['T1'])
BASE_URL = 'http://localhost:80/gilhari/v1'
endpoint = 'Employee'

def get_attribues(dept_number):
    url = f"http://localhost:80/jdx/v1/Department/getObjectById?filter=department_no={dept_number}"
    response = requests.get(f'http://localhost:80/jdx/v1/Department/getObjectById?filter=department_no={dept_number}')
    if response.status_code == 200:
        Number_of_E_before = response.json()['Nmuber_of_Employees']
        return Number_of_E_before
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}, Response: {response.text}")
        
def update_department_Number(Number_of_E_before,dept_number):
    url = f'http://localhost:80/jdx/v1/Department?filter=department_no={dept_number}'
    payload = {
    
    "newValues": ["Nmuber_of_Employees", Number_of_E_before+1]
    }
    response = requests.patch(url, json=payload)

# Check if the request was successful
    if response.status_code in [200, 204]:
        print("Department data updated successfully.")
    else:
        print(f"Failed to update data. Status code: {response.status_code}, Response: {response.text}")
    
    

try:
    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        message = json.loads(msg.value().decode('utf-8'))
        print(f"Consumed message from {msg.topic()}: {message}")
        print()
        entity_id = message['entity'][0]['id']
        dept_number=message['entity'][0]['department_no']
        Number_of_E_before=get_attribues(dept_number)
        update_department_Number(Number_of_E_before,dept_number)
        

        # Send the data to your microservice
        response = requests.post(f'{BASE_URL}/{endpoint}', json=message)

        if not 200 <= response.status_code < 300:
            print(f"Failed to send data to microservice: {response.text}")
finally:
    c.close()
