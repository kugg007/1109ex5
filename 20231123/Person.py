
class  Employee:
    def __init__(self,emp_id,emp_name,emp_salary,emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def calculate_emp_salary(self,worktime):
        self.overworktime = worktime - 50
        if self.overworktime>0:
            self.emp_salary =self.emp_salary +(self.overworktime*(self.emp_salary/50))
            print(f"{self.emp_id},{self.emp_name},{int(self.emp_salary)},{self.emp_department}\n")
        else:
            print(f"{self.emp_id},{self.emp_name},{int(self.emp_salary)},{self.emp_department}\n")
        

    def emp_assign_department(self,emp_department):
        self.emp_department = emp_department

    def print_employee_details(self):
        print(f"{self.emp_id},{self.emp_name},{int(self.emp_salary)},{self.emp_department}\n")

emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()
print("**********")
emp1.emp_assign_department("OPERATIONS")
emp2.emp_assign_department("SALES")
emp3.emp_assign_department("RESEARCH")
emp4.emp_assign_department("ACCOUNTING")

emp1.print_employee_details()
emp2.print_employee_details()
emp3.print_employee_details()
emp4.print_employee_details()
print("**********")
emp1.calculate_emp_salary(64)
emp2.calculate_emp_salary(46)
emp3.calculate_emp_salary(80)
emp4.calculate_emp_salary(37)