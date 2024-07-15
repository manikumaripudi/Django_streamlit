# import streamlit as st
# import django
# import os
# import sys

# # Set up Django environment
# sys.path.append(os.path.join(os.path.dirname(__file__), 'employee_project'))
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
# django.setup()

# from employee_app.models import Employee

# st.title("Employee Management System")

# # Sidebar for CRUD operations
# operation = st.sidebar.selectbox("Select an operation", ["Create", "Retrieve", "Update", "Delete"])

# if operation == "Create":
#     st.header("Create a New Employee")
#     name = st.text_input("Name")
#     email = st.text_input("Email")
#     salary = st.number_input("Salary", min_value=0)
#     address = st.text_area("Address")
#     if st.button("Submit"):
#         employee = Employee(name=name, email=email, salary=salary, address=address)
#         employee.save()
#         st.success("Employee created successfully")

# elif operation == "Retrieve":
#     st.header("Retrieve All Employees")
#     employees = Employee.objects.all()
    
#     if employees.exists():
#         # Display employees in a table
#         employee_data = [(employee.id, employee.name, employee.email, employee.salary, employee.address) for employee in employees]
#         st.table(employee_data)
#     else:
#         st.write("No employees found.")

# elif operation == "Update":
#     st.header("Update Employee Details")
#     employee_id = st.number_input("Employee ID", min_value=1, step=1)
#     if st.button("Load Employee"):
#         employee = Employee.objects.filter(id=employee_id).first()
#         if employee:
#             new_name = st.text_input("New Name", value=employee.name)
#             new_email = st.text_input("New Email", value=employee.email)
#             new_salary = st.number_input("New Salary", min_value=0, value=float(employee.salary),step=1.0)
#             new_address = st.text_area("New Address", value=employee.address)
#             if st.button("Update"):
#                 employee.name = new_name
#                 employee.email = new_email
#                 employee.salary = (new_salary)
#                 employee.address = new_address
#                 employee.save()
#                 st.success("Employee updated successfully")
#         else:
#             st.error("Employee not found")

# elif operation == "Delete":
#     st.header("Delete Employee")
#     del_employee_id = st.number_input("Employee ID to delete", min_value=1, step=1)
#     if st.button("Delete"):
#         del_employee = Employee.objects.filter(id=del_employee_id).first()
#         if del_employee:
#             del_employee.delete()
#             st.success("Employee deleted successfully")
#         else:
#             st.error("Employee not found")




import streamlit as st
import django
import os
import sys
from decimal import Decimal

# Set up Django environment
sys.path.append(os.path.join(os.path.dirname(__file__), 'employee_project'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_project.settings')
django.setup()

from employee_app.models import Employee

st.title("Employee Management System")

# Sidebar for CRUD operations
operation = st.sidebar.selectbox("Select an operation", ["Create", "Retrieve", "Update", "Delete"])

if operation == "Create":
    st.header("Create a New Employee")
    name = st.text_input("Name")
    email = st.text_input("Email")
    salary = st.number_input("Salary", min_value=0.0, step=0.01)
    address = st.text_area("Address")
    if st.button("Submit"):
        employee = Employee(name=name, email=email, salary=Decimal(salary), address=address)
        employee.save()
        st.success("Employee created successfully")

elif operation == "Retrieve":
    st.header("Retrieve All Employees")
    employees = Employee.objects.all()
    
    if employees.exists():
        # Display employees in a table
        employee_data = [(employee.id, employee.name, employee.email, employee.salary, employee.address) for employee in employees]
        st.table(employee_data)
    else:
        st.write("No employees found.")

elif operation == "Update":
    st.header("Update Employee Details")
    employee_id = st.number_input("Employee ID", min_value=1, step=1)

    employee = Employee.objects.filter(id=employee_id).first()
    if employee:
            st.text(f"Current Name: {employee.name}")
            new_name = st.text_input("New Name", value=employee.name)
            new_email = st.text_input("New Email", value=employee.email)
            new_salary = st.number_input("New Salary", min_value=0.0, value=float(employee.salary), step=0.01)
            new_address = st.text_area("New Address", value=employee.address)
            if st.button("Update"):
                employee.name = new_name
                employee.email = new_email
                employee.salary = Decimal(new_salary)  # Salary as Decimal
                employee.address = new_address
                employee.save()
                
                st.success(f"Employee {employee_id} updated successfully")

            else:
               st.error("Employee not found")

elif operation == "Delete":
    st.header("Delete Employee")
    del_employee_id = st.number_input("Employee ID to delete", min_value=1, step=1)
    if st.button("Delete"):
        del_employee = Employee.objects.filter(id=del_employee_id).first()
        if del_employee:
            del_employee.delete()
            st.success("Employee deleted successfully")
        else:
            st.error("Employee not found")
