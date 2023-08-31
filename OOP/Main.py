import customer_
import employee_
import random 

if random.randint(0,1) == 0: 
    x = customer_.Customer("Bob", "Jones", "Main Street")
    #c.print()
    x.firstName = "John" # Uses the setter function from customer_.py file
    x.print()
else: 
    x = employee_.Employee("Nick","Smith", "Sales")
    x.print()