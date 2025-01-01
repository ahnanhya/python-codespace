
name = input('Enter the employee\'s name: ')
id_number = input('Enter the employee\'s ID: ')
position = input('Enter the employee\'s position: ')
monthly_salary = float(input('Enter the employee\'s monthly salary: '))

employee = (name, id_number, position, monthly_salary)
gross_pay = employee[3] * 12
pf = gross_pay * 0.1
net_pay = gross_pay - pf

print("\n\n**EMPLOYEE PAYROLL")
print('Name:', employee[0])
print('ID:', employee[1])
print('Position:', employee[2])
print('Monthly Salary:', employee[3])
print('Gross Pay:', gross_pay)
print('PF:', pf)
print('Net Pay:', net_pay)
print("")
