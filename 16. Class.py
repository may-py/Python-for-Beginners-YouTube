#Object creation with class


class Users:
    pass

print(Users)

Users.first_name = 'Mayur'
Users.last_name = 'Suthar'

print(Users.first_name)
print(Users.last_name)




class Employees:
    def __init__(self):
        self.first_name = 'Mayur'
        self.last_name = 'Suthar'    
    

Employee1 = Employees()

print(Employee1.first_name)
print(Employee1.last_name)


class Employees:
    def __init__(self,first_name,last_name,salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def expected(self):
        return  self.salary + self.salary * 0.5

    def all_emp(self):
        print(f'Name is {self.first_name}, Family name is {self.last_name}, and salary is {self.salary} ')


Employee1 = Employees("Mayur","Suthar",10000)
Employee2 = Employees("ABC","XYZ",20000)

print(Employee2.first_name)
print(Employee2.last_name)
print(Employee2.salary)
print(Employee2.expected())
print(Employee2.all_emp())








