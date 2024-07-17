# Employee Management System and Motor Vehicle Dealership System using Apache Kafka as Streaming Service with Gilhari Microservice

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

- **javasrc**: Contains Java source code specific to database 2     (MySQL)
- **javasrcDB1**: Contains Java source code specific to database 1 (PostgreSQL).
- **src**: Contains other source code for the project.

For more detailed information on each folder, please refer to their respective README files:

- [javasrcDB2 README](javasrcDB2/README.md)
- [javasrcDB1 README](javasrcDB1/README.md)
- [src README](src/README.md)








