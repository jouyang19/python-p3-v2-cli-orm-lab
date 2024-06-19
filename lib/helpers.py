from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    [print(employee) for employee in Employee.get_all()]


def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    elif employee is None:
        print(f'Employee {name} not found')      
    else:
        print(f'Invalid input. Please try again.')
        


def find_employee_by_id():
    e_id = input("Enter the employee's ID: ")
    employee = Employee.find_by_id(e_id)
    if employee:
        print(employee)
    elif employee is None:
        print(f'Employee {e_id} not found')
    else:
        print("Invalid input. Please try again")


def create_employee():
    name = input("Enter employee's name: ")
    job_title = input("Enter employee's job title: ")
    department_id = input("Enter employee's department id: ")
    
    try:
        employee = Employee.create(name, job_title, int(department_id))
        print(f'Successfully created employee {employee}')
    except Exception as exc:
        print("Error creating employee: ", exc)


def update_employee():
    employee_id = int(input("Enter employee's id: "))
    employee = Employee.find_by_id(employee_id)
    if employee:
        try: 
            name = input("Enter employee's new name: ")
            job_title = input("Enter employee's new job title: ")
            department_id = input("Enter employee's new department id: ")
            if not name == "":
                employee.name = name
            if not job_title == "":
                job_title = job_title
            if not department_id == "":
                employee.department_id = int(department_id)
            employee.update()
            print(f'Successfully updated employee {employee}')
        except Exception as exc:
            print("Error creating employee: ", exc)

def delete_employee():
    employee_id = input("Enter employee id: ")
    employee = Employee.find_by_id(int(employee_id))
    if employee:
        employee.delete()
        print('Employee successfully removed')
    else:
        print('Employee 99 not found')


def list_department_employees():
    department_id = input("Enter department id: ")
    department = Department.find_by_id(int(department_id))
    if department:
        for employee in department.employees():
            print(employee)
    else:
        print(f'Department {department_id} not found')
        