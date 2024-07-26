# Employee Management System and Motor Vehicle Dealership System using Apache Kafka as Streaming Service with Gilhari Microservice hosted on Azure Cloud 

This example demonstrates the use and versatility of the Gilhari microservice for managing data across two different databases: PostgreSQL and MySQL. By effectively utilizing Gilhari, we showcase a seamless and user-friendly approach to storing different Kafka topics in distinct databases.

- **Employee Management System**: Data related to employees, such as their personal information, job details, and departmental assignments, is streamed and stored in MySQL. This ensures robust and scalable management of employee records.

- **Motor Vehicle Dealership System**: Data related to vehicle inventory, sales, and customer information is streamed and stored in PostgreSQL. This setup allows for efficient handling and querying of dealership operations.

- **Kafka Topics**: Two Kafka topics are utilized:
  - **Topic 1**: Streams data related to the Employee Management System and routes it to the MySQL database.
  - **Topic 2**: Streams data related to the Motor Vehicle Dealership System and routes it to the PostgreSQL database.

- **Gilhari Microservice**: Acts as a mediator to ensure smooth data flow between Kafka topics and the respective databases. It provides:
  - Seamless integration with both PostgreSQL and MySQL.
  - High reliability and fault tolerance in data streaming and storage.

- **Database Tables**:
  - **PostgreSQL**:
    - `Vehicle`
    - `Buyer`
  - **MySQL**:
    - `Employee`
    - `Department`

By leveraging the capabilities of Kafka and Gilhari, this example illustrates a powerful solution for managing distinct data systems efficiently and effectively.

## Folders

This repository contains the following folders:

- **javasrc**: Contains Java source code specific to database 2     (Azure MySQL)
- **javasrcDB1**: Contains Java source code specific to database 1 (Azure PostgreSQL).
- **src**: Contains other source code for the project.

For more detailed information on each folder, please refer to their respective README files:

- [javasrcDB2 README](javasrcDB2/README.md)
- [javasrcDB1 README](javasrcDB1/README.md)
- [src README](src/README.md)

## How to Deploy on Azure Cloud

1. **Login to the Azure portal**
    - Open the Azure portal and log in with your email account.

2. **Create Azure Databases**
    - Create a MySQL Azure database by filling in the necessary details.
    - Create a PostgreSQL Azure database by filling in the necessary details.

3. **Setup Local Database Management Tools**
    - For MySQL, create a new server in MySQL Workbench using the Azure database details.
    - For PostgreSQL, create a new server in pgAdmin using the Azure database details.

4. **Configure Database Connections**
    - In the mapping files of the `javasrcDB1` and `javasrcDB2` folders, update the server name and credentials to point to the Azure cloud databases instead of the local systems databases.



## Running the Project

1. **Clone the Repository**
    ```sh
    git clone https://github.com/SagarThomas24/Gilhari10_KafkaStreamingService
    cd yourrepository
    ```
2. **Run the Docker Compose**
    - Ensure the Docker daemon is running.
    - Run the following command to start the services:
    ```sh
    docker-compose up -d
    ```
5. **Fill Database Tables Before startingthe streaming service**
    - Once all the necessary Kafka and microservices are running, fill in the database tables by running the following Python scripts:
    ```sh
    python department.py  # For MySQL database
    python vehicle.py     # For PostgreSQL database
    ```








