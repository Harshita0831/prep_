##design a console based "Employee Payroll system" using oops python
##the system should calculate salary for different types of employees using all oops concept

##employee - abstract class
##full time employee - child class
#part time employee - child class
#salary - encapsulated data
#payroll system - controller(HAS-A)

#output
#Employee reated
##Salary:50000
#Employee Created
#Salary:40000

class Employee:
    def __init__(self,emp_id,name):
        self.emp_id = emp_id
        self.name = name
    def calculate_salary(self):
        pass
class FullTimeEmployee(Employee):
    def __init__(self,emp_id,name,monthly_salary):
        super().__init__(emp_id,name)
        self._monthly_salary = monthly_salary
        #encapsulation because salary is protected
    def calculate_salary(self):
        return self._monthly_salary
class PartTimeEmployee(Employee):
    def __init__(self,emp_id,name,hours_worked,rate_per_hour):
        super().__init__(emp_id,name)
        self._hours_worked = hours_worked
        self._rate_per_hour = rate_per_hour
    def calculate_salary(self):
        return self._hours_worked*self._rate_per_hour
    
class PayRollApp:
    def __init__(self):
        self.employee = None
    def create_employee(self,emp_type):
        if emp_type == "FullTime":
            self.employee=FullTimeEmployee(1,"Amit",5000)
        else:
            self.employee=PartTimeEmployee(2,"Neha",80,500)
        return "Employee Created"
    def get_salary(self):
        return self.employee.calculate_salary()
app=PayRollApp()
print(app.create_employee("FullTime"))
print("Salary:",app.get_salary())
app2 = PayRollApp()
print(app.create_employee("PartTime"))
print("Salary:",app.get_salary())
    































