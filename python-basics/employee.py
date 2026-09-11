# employee_name ="Arjun Das"
# employee_email ="abc@gmail.com"
# employee_age = 25

# print(employee_name)
# print(employee_email)
# print(employee_age)


# CREATE AN EMPLOYEE

# name ="Riya Roy"
# age = 30
# salary = 30000

# print("Name:", name)
# print("Age:", age)
# print("Salary", salary)

# CONDITIONS

# name ="Riya Roy"
# is_active = True

# if is_active:
#     print(name +" " +"is Active");
# else:
#     print("Employee is not Active");

# USE f-string 

# name ="Riya Roy"
# is_active = True

# if is_active:
#     print(f"{name} is Active");
# else:
#     print("Employee is not Active");


# USE FUNCTIONS

# def display_employee(name, salary):
#     print("Employee:", name)
#     print("Salary:", salary)


# display_employee("Arjun Das", 55000)
# display_employee("Rahul Sen", 60000)

# List

employees =["Arjun das", "Riya Roy", "Rahul Sharma", "Amit Nag"]

# print(employees)
# print(employees[0])

# for employee in employees:
#     print(employee[3])


#DICTIONARY

# employee = {

#     "id": 1,
#     "name" : "Arjun Das",
#     "email" : "arjun@gmail.com",
#     "age" : 35,
#     "salary" : 30000
# }

# print(employee["name"])
# print(f"{employee['salary']}")


# EMPLOYEE DATASET

# employees = [
#     {
#         "id": 1,
#         "name" : "Arjun Das",
#         "email" : "arjun@gmail.com",
#         "age" : 35,
#         "salary" : 30000
#     },

#     {
#         "id": 2,
#         "name" : "Riya Roy",
#         "email" : "riya@gmail.com",
#         "age" : 30,
#         "salary" : 29000
#      },

#       {
#              "id": 3,
#              "name" : "Rahul Sharma",
#              "email" : "rahul@gmail.com",
#              "age" : 40,
#              "salary" : 50000
#       }

# ]

# for employee in employees:

#     # print(f"Employee name is: {employee ['name']}")

#     print(
#         employee["id"],
#         employee["name"],
#         employee["salary"]
#     )


# COMPAIRING VALUES

# salary = 55000

# if(salary >= 80000):
#     print("Senior Level Employee")

# elif (salary >= 50000):
#     print("Mid Level Manager")

# else:
#     print("Junior Level Employee")

## WITHOUT PARAMETER FUNCTION

def say_hello():
    print("Hello, World")

say_hello()

## WITH PARAMETER FUNCTION

def employee(name):
    print(f"Employee name is: {name}")


employee("Arjun Das")


## FUNCTION WITH RETURN VALUE

def calculate_salary(salary, bonus):
    total_salary = salary + bonus
    return total_salary

total = calculate_salary(50000, 3000)
print(f"Total Salary is:{total}")