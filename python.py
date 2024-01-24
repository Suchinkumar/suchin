class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


class EmployeeTable:
    def __init__(self, employees):
        self.employees = employees

    def sort_table(self, sort_key):
        if sort_key == 1:
            self.employees.sort(key=lambda emp: emp.age)
        elif sort_key == 2:
            self.employees.sort(key=lambda emp: emp.name)
        elif sort_key == 3:
            self.employees.sort(key=lambda emp: emp.salary)
        else:
            print("Invalid sorting option.")

    def print_table(self):
        for emp in self.employees:
            print(emp)


def main():
    employees_data = [
        Employee("161E90", "Ramu", 35, 59000),
        Employee("171E22", "Tejas", 30, 82100),
        Employee("171G55", "Abhi", 25, 100000),
        Employee("152K46", "Jaya", 32, 85000),
    ]

    employee_table = EmployeeTable(employees_data)

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        sort_option = int(input("Enter your choice (1/2/3): "))
        employee_table.sort_table(sort_option)
        print("\nSorted Employee Table:")
        employee_table.print_table()

    except ValueError:
        print("Invalid input. Please enter a number (1/2/3).")


if __name__ == "__main__":
    main()
