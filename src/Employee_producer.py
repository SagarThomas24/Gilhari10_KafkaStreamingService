from confluent_kafka import Producer
import json
import random
import time  # import the time module
from datetime import datetime

t = Producer({'bootstrap.servers': 'localhost:9092'})



date_str = '1990-01-01'
date_time_obj = datetime.strptime(date_str, '%Y-%m-%d')
timestamp = int(date_time_obj.timestamp() * 1000)


while True:
    k_input = input("Enter starting ID to produce 20 employees or 'exit' to stop: ")
    if k_input.lower() == 'exit':
        break

    # Convert input to integer
    k = int(k_input)

    for i in range(k, k+20):  # Producing 20 employee entities starting from ID k
        entity = {
            "id": i,
            "exempt": random.choice([True, False]),
            "compensation": random.randint(100000, 400000),
            "name": f"emp{i}",
            "department_no": random.randint(1, 5),
            "DOB": timestamp
        }

        message = {"entity": [entity]}

        t.produce('T1', json.dumps(message).encode('utf-8'))
        t.flush()
        time.sleep(2)  # Optional: pause for 2 seconds