# Writing employee details to a file
with open('employee_details.txt', 'w') as file:
 file.write("101, John Doe, Manager\n")
 file.write("102, Jane Smith, Developer\n")

# Reading from the file
with open('employee_details.txt', 'r') as file:
 print("Employee Details:")
 print(file.read())

# Appending new employee details to the file
with open('employee_details.txt', 'a') as file:
 file.write("103, Alice Johnson, HR\n")

# Reading the updated file content
with open('employee_details.txt', 'r') as file:
 print("\nUpdated Employee Details:")
 print(file.read())