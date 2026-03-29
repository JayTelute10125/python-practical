import pandas as pd

# Read the Excel file
df_emp = pd.read_excel('employee.xlsx')

# a) Employees in "Automotive" domain
automotive_team = df_emp[df_emp['Department'] == 'Automotive']
print("Automotive Employees:\n", automotive_team)

# b) Details of an employee by ID (Input from user)
try:
    emp_id = int(input("Enter Employee ID to search: "))
    specific_emp = df_emp[df_emp['Employee ID'] == emp_id]
    if not specific_emp.empty:
        print("Employee Details:\n", specific_emp)
    else:
        print(f"No employee found with ID {emp_id}")
except ValueError:
    print("Invalid input! Please enter a valid integer Employee ID.")

# d) List of all Developers
developers = df_emp[df_emp['Designation'] == 'Developer']
print("All Developers:\n", developers)