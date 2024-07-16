import json
import requests
from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'myg',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['T2'])
BASE_URL = 'http://localhost:88/gilhari/v1'
endpoint = 'Buyer'

def get_attributes(Vehicle_id):
    response = requests.get(f'http://localhost:88/jdx/v1/Vehicle/getObjectById?filter=Vehicle_id={Vehicle_id}')
    if response.status_code == 200:
        Number_of_V_before = response.json()['No_of_vehicles']
        return Number_of_V_before
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}, Response: {response.text}")
        
def update_Vehicle_Number(Number_of_V_before,Vehicle_id):
    url = f'http://localhost:88/jdx/v1/Vehicle?filter=Vehicle_id={Vehicle_id}'
    if(Number_of_V_before>1):
        
        payload = {
    
        "newValues": ["No_of_vehicles", Number_of_V_before-1]
        }
    else:
        payload = {
    
        "newValues": ["No_of_vehicles", 50]
        }
    response = requests.patch(url, json=payload)
    
    
    
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
        
        Vehicle_id = message['entity'][0]['Vehicle_id']
        Number_of_V_before=get_attributes(Vehicle_id)
        update_Vehicle_Number(Number_of_V_before,Vehicle_id)
        
        response = requests.post(f'{BASE_URL}/{endpoint}', json=message)

        if not 200 <= response.status_code < 300:
            print(f"Failed to send data to microservice: {response.text}")
finally:
    c.close()
        