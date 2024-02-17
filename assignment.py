class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def assign_department(self, new_department):
        self.emp_department = new_department

    def print_employee_details(self):
        print("Employee ID:", self.emp_id)
        print("Employee Name:", self.emp_name)
        print("Employee Salary:", self.emp_salary)
        print("Employee Department:", self.emp_department)

    def calculate_emp_salary(self, hours_worked):
        if hours_worked > 50:
            overtime = hours_worked - 50
            overtime_amount = overtime * (self.emp_salary / 50)
            total_salary = self.emp_salary + overtime_amount
            return total_salary
        else:
            return self.emp_salary

emp1 = Employee("001", "John Doe", 50000, "HR")
emp1.print_employee_details()

emp1.assign_department("Finance")
emp1.print_employee_details()

total_salary = emp1.calculate_emp_salary(55)
print("Total Salary:", total_salary)


#Question 2 answer
class Restaurant:
    def _init_(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, item_price):
        self.menu_items[item_name] = item_price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, table_number, order):
        self.customer_orders.append({"table_number": table_number, "order": order})

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("Booked Tables:")
        print(self.booked_tables)

    def print_customer_orders(self):
        print("Customer Orders:")
        for order in self.customer_orders:
            print(f"Table {order['table_number']}: {order['order']}")


restaurant = Restaurant()


restaurant.add_item_to_menu("Pizza", 10)
restaurant.add_item_to_menu("Burger", 8)
restaurant.add_item_to_menu("Pasta", 12)


restaurant.book_table(1)
restaurant.book_table(3)


restaurant.customer_order(1, "Pizza")
restaurant.customer_order(3, "Burger and Pasta")


restaurant.print_menu()


restaurant.print_table_reservations()

restaurant.print_customer_orders()