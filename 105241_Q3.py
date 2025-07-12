# This script implements a simple employee and department management system.
# 105241_Q3.py
# Class: Employee and Department Management System

class Employee:
    def __init__(self, name, employee_id, salary):
        # Initialize employee attributes
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        """Display employee details"""
        print(f"Employee: {self.name} (ID: {self.employee_id})")
        print(f"Salary: ${self.salary:.2f}")
        print("-" * 30)

    def update_salary(self, new_salary):
        """Update employee's salary"""
        self.salary = new_salary
        print(f"Updated salary for {self.name}: ${new_salary:.2f}")


class Department:
    def __init__(self, department_name):
        # Initialize department attributes
        self.department_name = department_name
        self.employees = []  # List to store Employee objects

    def add_employee(self, employee):
        """Add an employee to the department"""
        self.employees.append(employee)
        print(f"Added {employee.name} to {self.department_name}")

    def total_salary_expenditure(self):
        """Calculate total salary expenditure for the department"""
        total = sum(emp.salary for emp in self.employees)
        print(f"\nTotal salary expenditure for {self.department_name}: ${total:.2f}")
        return total

    def display_all_employees(self):
        """Display all employees in the department"""
        print(f"\nEmployees in {self.department_name}:")
        if not self.employees:
            print("No employees in this department")
            return

        for i, emp in enumerate(self.employees, 1):
            print(f"{i}. {emp.name} (ID: {emp.employee_id}) - Salary: ${emp.salary:.2f}")

    # Search for an employee by ID
    def search_employee_by_id(self, employee_id):
        """Search for an employee by their ID"""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                print("\nEmployee found:")
                emp.display_details()
                return
        print("\nNo employee found with the given ID.")

def main():
    # Create department
    print("=== Employee & Department Management System ===")
    dept_name = input("Enter department name: ")
    department = Department(dept_name)

    while True:
        print("\n=== Menu ===")
        print("1. Add an employee")
        print("2. Update an employee's salary")
        print("3. Display total salary expenditure")
        print("4. Display all employees")
        print("5. Search for an employee by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): Others will be ignored: ")

        if choice == '1':
            # Add new employee
            print("\n=== Add Employee ===")
            name = input("Enter employee name: ")
            emp_id = input("Enter employee ID: ")

            # Validate salary input
            while True:
                try:
                    salary = float(input("Enter salary: $"))
                    if salary < 0:
                        print("Salary cannot be negative")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a number")

            new_emp = Employee(name, emp_id, salary)
            department.add_employee(new_emp)

        elif choice == '2':
            # Update employee salary
            print("\n=== Update Salary ===")
            if not department.employees:
                print("No employees in department")
                continue

            department.display_all_employees()

            try:
                emp_index = int(input("Enter employee number to update: ")) - 1
                if 0 <= emp_index < len(department.employees):
                    # Validate new salary input
                    while True:
                        try:
                            new_salary = float(input("Enter new salary: $"))
                            if new_salary < 0:
                                print("Salary cannot be negative")
                                continue
                            break
                        except ValueError:
                            print("Invalid input. Please enter a number")

                    department.employees[emp_index].update_salary(new_salary)
                else:
                    print("Invalid employee number")
            except ValueError:
                print("Please enter a valid number")

        elif choice == '3':
            # Display total salary expenditure
            print("\n=== Salary Expenditure ===")
            department.total_salary_expenditure()

        elif choice == '4':
            # Display all employees
            print("\n=== Department Employees ===")
            department.display_all_employees()

        elif choice == '5':
            # Search for an employee by ID
            print("\n=== Search Employee ===")
            emp_id = input("Enter employee ID to search: ")
            department.search_employee_by_id(emp_id)

        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# This code implements a simple employee and department management system.
if __name__ == "__main__":
    main() # Entry point for the program

# End of script.