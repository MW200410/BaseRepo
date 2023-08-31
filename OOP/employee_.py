import Person_
class Employee(Person_.Person):
    def __init__(self, firstname, lastname, department):
        super().__init__(firstname, lastname)
        self.department = department
    
    def print(self):
        print(f"Department: {self.department}, ", end ='Name: ')# Prints the department defined in this Employee class.
        super().print() # uses the print function from superclass -> Person