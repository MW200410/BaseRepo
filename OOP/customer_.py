import Person_
class Customer(Person_.Person):
    def __init__(self, firstname, lastname, address): # defines a constructor for this Customer class
        super().__init__(firstname, lastname) # calls contructor in the superclass-> Person
        self.address = address 

    def print(self):
        print(f"Address: {self.address}, ", end ='Name: ')# Prints the address defined in this Customer class.
        super().print() # uses the print function from superclass -> Person




    