employees = []


# CREATE
def add_employee(name, department, salary):

    employee = {
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)


# Add employees
add_employee("Riya Roy", "IT", 30000)
add_employee("Arjun Das", "HR", 40000)
add_employee("Rahul Sharma", "Finance", 25000)


# READ
def display_employees():

    for employee in employees:
        print(
            employee["name"],
            employee["department"],
            employee["salary"]
        )


# UPDATE
def update_salary(name, new_salary):

    for employee in employees:

        if employee["name"] == name:
            employee["salary"] = new_salary
            print("Salary updated")
            return

    print("Employee not found")


# Update employee
update_salary("Riya Roy", 35000)

# Display employees
display_employees()