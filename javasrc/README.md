# Gilhari Microservice Setup

This file lists out the steps taken to configure the Gilhari microservice . In this example, the classes named `Employee`, `Department` are created and mapped as follows.

## Step 1: Define and Compile Empty Java (Container) Class

1. In `src/main/java/models`, create a class file `JSON_Employee.java`  (derived from Software Tree's JDX).
2. Similarly, create class files `JSON_Department.java`.

3. In the `lib/` directory, add the required .jar files `json-20160212.jar` and `jxclasses.jar` found in the gilhari SDK `lib\` directory.

4. In a terminal, navigate to `./javasrc` and run the following command to compile `JSON_Employee.java`:
    ```bash
    javac -cp "lib/json-20160212.jar:lib/jxclasses.jar" -d bin src/main/java/models/JSON_Employee.java
    ```
5. Also compile the `JSON_Department.java` using the command:
    ```bash
    javac -cp "lib/json-20240303.jar:lib/jxclasses.jar" -d bin src/main/java/models/JSON_Department.java
    
    ```

## Step 2: Define a Declarative Object Relational Mapping (ORM) Specification and Gilhari Configuration

1. In the `config/` directory, create a file named `gilhari10_hr_MySQL.jdx` as shown.
2. Add the database's JDBC driver (e.g., MySQL's) as a .jar file to `config/`.
3. Add a file `classnames_map_example.js` to `config/` to map "Employees" to the defined `Employee` container class. Repeat the same for the other  class.
4. Add a file `gilhari10_hr_mysql_service.config` to `javasrc/` and fill in the required fields. Refer to the Gilhari documentation for more information on the .config file and its fields.

## Step 3: Create a Dockerfile, Build and Run the Container

1. Create the Dockerfile as shown in the project directory.
2. Build the Docker image using the following command:
    ```bash
    docker build -t my_app_gilhari -f ./Gilhari10_Mysql .
    ```
    `my_app_gilhari`- this could be any name of your choice.

3. Run the Docker image using the command:
    ```bash
    docker run -p 80:8081 my_app_gilhari
    ```

By following these steps, you can successfully configure the Gilhari microservice with JDX ORM, defining and mapping the `Employee`, `Department` classes, and running the service in a Docker container.









