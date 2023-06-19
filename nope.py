n1=int(input("Enetr n1: "))
n2=int(input("Enetr n1: "))
# sirst
def euclidean(a,b):
    while a!=b:
        if a > b:
            a-=b
        else:
            b-=a
    return a or b
print(f"Gcd of a and b is:{euclidean(n1,n2)}")
# second
def gcd(x,y):
    if x<y:
        x,y=y,x
    if x%y==0:
        return y
    else:
        return gcd(y,x%y)
print(gcd(n1,n2))     

def GCD(m,n):
    lm = []
    ln= []
    common_factors = []
    for i in range(1,m+1):
        if m%i == 0:
            lm.append(i)
    for j in range(1,n+1):
        if n%j == 0:
            ln.append(j)
    for x in lm:
        if x in ln:
            common_factors.append(x)
    return common_factors[-1] or max(common_factors)
print(GCD(n1,n2))
try:          
    file_1 = r'Downloads/quantum.txt'
    file_2 = r'OneDrive/Desktop/Gusus.txt'
    with open(file_1,'r') as f1:
        with open(file_2,'w') as f2:
            for line in f1:
                mod = line.replace(' ','.') \
                    .swapcase()
                f2.write(line)
    print('File edited successfully')
except FileNotFoundError:
    print('Sorry file not found')
    
                
class EMPLOYEE:
        
    total_employees = 0
    total_male = 0
    total_female = 0
    salary_above_10000 = []
    asst_mangager = []
        
    def __init__(self,name,design,gender,DOJ,salary):# here we have given attributes and constructing an object
        
        self.name = name
        self.design = design 
        self.gender = gender
        self.DOJ = DOJ
        self.salary = salary
        EMPLOYEE.total_employees += 1
        
    if gender == 'Male':
        
        EMPLOYEE.total_male += 1    
        
    elif gender == 'Female':
        
        EMPLOYEE.total_female += 1
        
    if salary > 10000:
        
        EMPLOYEE.salary_above_10000.append()
        
    if design == 'Assistant Manager':
        
        EMPLOYEE.asst_manager.append()

# Now we create employee (as objects)
em1 = EMPLOYEE('John Wick','Assistant Manager','Male',"2018-09-12",15000)
em2 = EMPLOYEE('Sarah Smith','Manager','Female','2017-01-05',20000)
em3 = EMPLOYEE("Mike Johnson", "Assistant Manager", "Male", "2019-03-01", 12000)
em4 = EMPLOYEE("Emily Davis", "Receptionist", "Female", "2020-04-10", 8000)


total_employee = EMPLOYEE.total_employees
total_male = EMPLOYEE.total_male
total_female = EMPLOYEE.total_female
salary_above_10000 = EMPLOYEE.salary_above_10000
asst_manager = EMPLOYEE.asst_mangager

print("Total employees:", total_employees)
print("Male count:", male_count)
print("Female count:", female_count)
print("Employees with salary above 10000:")

for employee in salary_above_10000:
    print(employee.name)
print("Assistant Manager: ")
for employee in asst_manager:
    print(employee.name)
    
    

    