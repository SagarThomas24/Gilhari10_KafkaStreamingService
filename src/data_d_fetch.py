import requests
employee_id = 18 # Define the variable for the employee ID

# Use string formatting to include the variable in the URL
url = f"http://localhost:80/gilhari/v1/Employee/getObjectById?filter=id={employee_id}"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    employee = response.json()
    d_no = int(response.json()['dno'])
    # Print the retrieved Employee object
    print(d_no)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}, Response: {response.text}")
# Define the URL for retrieving Department data

url = "http://localhost:80/jdx/v1/Department/getObjectById?filter=dno={d_no}"

# Send a GET request to the URL
response = requests.get(f'http://localhost:80/jdx/v1/Department/getObjectById?filter=dno={d_no}')

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    Number_of_E_before = response.json()['Nmuber_of_Employees']
    # Print the retrieved Department data
    
    print(Number_of_E_before)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}, Response: {response.text}")
    


# Define the URL for updating the Employee data
department_number = 3  # This variable represents the department number

# Use string formatting to include the variable in the URL
url = f'http://localhost:80/jdx/v1/Department?filter=dno={d_no}'

# Define the payload for the update
payload = {
    
    "newValues": ["Nmuber_of_Employees", Number_of_E_before+1]
}

# Send a PATCH or PUT request to the URL with the payload
# Use PATCH if you're partially updating the resource, or PUT if you're replacing it entirely.
# This example uses PATCH.
response = requests.patch(url, json=payload)

# Check if the request was successful
if response.status_code in [200, 204]:
    print("Employee data updated successfully.")
else:
    print(f"Failed to update data. Status code: {response.status_code}, Response: {response.text}")