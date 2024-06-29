from confluent_kafka import Producer
import json
import random
import time  # import the time module

p = Producer({'bootstrap.servers': 'localhost:9092'})




while True:
    k_input = input("Enter starting ID to produce 20 Buyers or 'exit' to stop: ")
    if k_input.lower() == 'exit':
        break

    # Convert input to integer
    k = int(k_input)

    for i in range(k, k+20):  # Producing 20 employee entities starting from ID k
        entity = {
            "Vehicle_id": random.randint(1, 5),
            "Buyer_id": i,
            "price": random.randint(100000, 400000),
            "Phone_Number":  random.randint(100000000, 999999999)
        }

        message = {"entity": [entity]}

        p.produce('T2', json.dumps(message).encode('utf-8'))
        p.flush()
        time.sleep(2)  # Optional: pause for 2 seconds