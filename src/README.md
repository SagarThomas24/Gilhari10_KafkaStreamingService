# Configuring and Running Kafka

This document provides an overview of the Python scripts used for producing and consuming Kafka messages, as well as managing vehicle and department data. It also includes instructions for running these scripts.

## Source Files Overview

### Producer Scripts
- **`Buyer_producer.py`**: Produces buyer data and sends it to Kafka topic `T2`.
- **`Employee_producer.py`**: Produces employee data and sends it to Kafka topic `T1`.

### Consumer Script
- **`emp_consumer.py`**: Consumes employee data from Kafka topic `T1` and updates the department's number of employees in the database.

-**`Buyer_consumer.py`** : Consumes Buyer data from Kafka topic `T2` and updates the Vehicle's number of Vechicles remaining in the database.

### Data Management Scripts
- **`Vehicle.py`**: Sends predefined vehicle data to the Gilhari microservice.
- **`Department.py`**: Sends predefined department data to the Gilhari microservice.

### Configuration File
- **`docker-compose.yml`**: Defines services, networks, and volumes for Docker containers.Make the necessary according to your Ipv4 address.

## How to Run the Scripts

### Docker-compose.yml
1. Navigate to the `src\` directory.
2. Run the script:
    ```bash
    docker-compose up-d
    ```

### Department Data
1. Navigate to the directory containing `Department.py`.
2. Run the script:
    ```bash
    python Department.py
    ```

### Vehicle Data
1. Navigate to the directory containing `Vehicle.py`.
2. Run the script:
    ```bash
    python Vehicle.py
    ```

### Buyer Producer
1. Navigate to the directory containing `Buyer_producer.py`.
2. Run the script:
    ```bash
    python Buyer_producer.py
    ```

### Employee Producer
1. Navigate to the directory containing `Employee_producer.py`.
2. Run the script:
    ```bash
    python Employee_producer.py
    ```

### Employee Consumer
1. Navigate to the directory containing `emp_consumer.py`.
2. Run the script:
    ```bash
    python emp_consumer.py
    ```
###  Buyer Consumer
1. Navigate to the directory containing `emp_consumer.py`.
2. Run the script:
    ```bash
    python Buyer_consumer.py
    ```





## Docker Configuration

To set up the Kafka and other necessary services using Docker, use the provided `docker-compose.yml` file. This file defines the necessary services, networks, and volumes.

### Running Docker Compose
1. Navigate to the directory containing `docker-compose.yml`.
2. Start the services:
    ```bash
    docker-compose up-d
    ```

## Notes
- Ensure that Kafka and any other dependencies are properly set up and configured before running the scripts.
- Update the configuration files as needed to match your specific environment and requirements.
- Remember to always first run ` Vehicle.py` and `department.py` before running any other producer and consumer scripts.









