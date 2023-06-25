class Employee:
    # defining class variables 
    employee_count = 0
    male = 0
    female = 0
    salary_10k = 0
    Assistant_mng = 0
 
    def __init__(self):
        Employee.employee_count += 1
        self.name = input("Name of employee: ")
        self.designation = input("Designation of employee: ")
        self.gender = input("Employee gender (m=male,f=female): ")
        self.DOJ = input("Enter DOJ: ")
        self.salary = int(input("Salary of employee: "))
        self.check()

    def check(self):
        if self.designation.lower == "asst mng":
            Employee.Assistant_mng += 1
        
        if self.gender == "m":
            Employee.male += 1
        else:
            Employee.female += 1
            
        if self.salary > 10000:
            Employee.salary_10k += 1
        
        return None
    def emp_count():
        return Employee.employee_count
    
    def male_count():
        return Employee.male
    
    def female_count():
        return Employee.female
    
    def asst_mng_count():
        return Employee.Assistant_mng
    
    def salary():
        return Employee.salary_10k
    
n = int(input("Enter total number of employees: "))

employees = []
for i in range(n):
    emp = Employee()
    employees.append(emp)
    
print("Total number of employees:", Employee.emp_count())
print("Number of male employees:", Employee.male_count())
print("Number of female employees:", Employee.female_count())
print("Number of employees with salary greater than 10,000:", Employee.salary())
print("Number of employees with designation 'Asst Manager':", Employee.asst_mng_count())