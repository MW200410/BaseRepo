# Don't Repeat Yourself [DRY] 

def print_item():
    print("Example")

print_item()


def print_name(firstName, LastName):
    print(firstName + " " + LastName)

print_name("bob","smith")


def full_name(firstName, LastName):
    return firstName + " " + LastName

print(full_name("bob","smith"))


def Print_Name(full_name_output):
    print(full_name_output)

Print_Name(full_name("Adam","Smith"))
