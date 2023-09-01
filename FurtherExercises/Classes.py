print("nQ1a\n")
# Q1a: Create a class which of a country (include continent, climate, language etc in the inputs)

# A1a:
class UK():
    def __init__(self, continent, climate, language):
        self.continent = continent
        self.climate = climate
        self.language = language
    
    def print(self):
        print(self.continent, self.climate, self.language)
        
united_kingdom = UK("Europe", "Temperate","English")
united_kingdom.print()


print("\nQ1b\n")
# Q1b: Create a subclass of a city which inherits from the country class

# A1b:

class Manchester(UK):
    def __init__(self, continent, climate, language, dialect):
        super().__init__(continent, climate, language)
        self.dialect = dialect

    def print(self): 
        print(f"{self.dialect}, ", end ='') # Prints the dialect defined in this Manchester class.
        super().print() # uses the print function from superclass -> UK


M = Manchester("Europe", "Damp", "English","Mancunian")
M.print()



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: Using the predefined class and is_prime method below, loop through list_of_numbers and create
# a list of primes from that list
list_of_numbers = [1, 12, 44, 53, 6, 3, 6545, 76, 32, 345, 22, 17, 19, 223, 156]


class Number:
    def __init__(self, integer):
        self.integer = integer

    def is_prime(self):
        if self.integer >= 2:
            #print(self.integer)
            for x in range(2, self.integer):
                if self.integer % x == 0:
                    #print("not prime",self.integer)
                    return False
            else:
                #print("primes",self.integer)
                return True
        
        else:
            #print("not prime",self.integer)
            return False


    def divisible_by_n(self, n):
        if self.integer % n == 0:
            return True
        else:
            return False
        

new_list = []
# A2a:
for i in list_of_numbers:
    if Number(i).is_prime() == True:
        new_list.append(i)
print("Primes:",new_list)


print("\nQ2b\n")
# Q2b: Now create a list of numbers from list_of_numbers that are divisible
# by both 3 and 4 using the divisible_by_n method above

# A2b:
listA = []

for i in list_of_numbers:
    if Number(i).divisible_by_n(3) == True and Number(i).divisible_by_n(4) == True:
        listA.append(i)
print(listA)



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Fix the following class and subclass (uncomment by selecting all rows and pressing CTRL + /)


class Boss(object):
    def __init__(self, name, attitude, behaviour, face):
        self.name = name
        self.attitude = attitude
        self.behaviour = behaviour
        self.face = face

    def get_attitude(self):
        return self.attitude

    def get_behaviour(self):
        return self.behaviour

    def get_face(self):
        return self.face


class GoodBoss(Boss):
    def __init__(self, name, attitude, behaviour, face):
        super().__init__(name, attitude,behaviour,face)

    def encourage(self):
       print(f"The team cheers for {self.name}, starts shouting awesome slogans then gets back to work.")


# A3a:


# -------------------------------------------------------------------------------------- #
