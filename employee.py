class Employee:
    
    NUMBER_OF_EMPLOYEE = 0
    RAISE_AMOUNT = 1.04
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        
        Employee.NUMBER_OF_EMPLOYEE += 1
        
    def __repr__(self):
        return f"Employee('{self.first_name}', '{self.last_name}', {self.salary})"
    
    def __str__(self):
        return f'{self.fullname} - {self.email}'
        
    def __add__(self, other):
        return self.salary + other.salary
    
    def __len__(self):
        return len(self.fullname())
    
    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @fullname.setter
    def fullname(self, name):
        first_name, last_name = name.split(' ')
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def email(self):
        return f'{self.first_name}.{self.last_name}@company.com'

    def apply_raise(self):
        self.salary = int(self.salary * self.RAISE_AMOUNT)
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.RAISE_AMOUNT = amount
        
    @classmethod
    def from_string(cls, string):
        "Construct an Employee from a STRING seperated by '-'"
        first_name, last_name, salary = string.split('-')
        return cls(first_name, last_name, salary)
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 4 or day.weekday() == 5:
            return False
        return True
    

class Developer(Employee):
    RAISE_AMOUNT = 1.10
    
    def __init__(self, first_name, last_name, salary, prog_lang):
        super().__init__(first_name, last_name, salary)
        self.prog_lang = prog_lang
        

class Manager(Employee):
    def __init__(self, first_name, last_name, salary, employees=None):
        super().__init__(first_name, last_name, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
            
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            
    def del_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            
    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

    
if __name__ == '__main__':
    pass
    