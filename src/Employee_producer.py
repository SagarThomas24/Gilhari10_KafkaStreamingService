from confluent_kafka import Producer
import json
import random
import time  # import the time module

p = Producer({'bootstrap.servers': 'localhost:9092'})




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
            "dno": random.randint(1, 5),
            "DOB": 110100
        }

        message = {"entity": [entity]}

        p.produce('T1', json.dumps(message).encode('utf-8'))
        p.flush()
        time.sleep(2)  # Optional: pause for 2 seconds