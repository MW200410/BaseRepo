def Add(x, y):
    return x+y 

def Subtract(x,y):
    return x-y 

def Multiply(x,y):
    return x*y

def Divide(x,y):
    return x/y

choice = int(input("\nEnter the value: 1 for Addition -- 2 for Subtraction -- 3 for Multiplaction -- 4 for Division: -> "))
 
x = float(input("\nInput your first number here: "))
y = float(input("\nInput your second number here: "))

if choice == 1:
    print(x, '+', y, '=', Add(x,y))
elif choice == 2:
    print(x, '-', y, '=', Subtract(x,y))
elif choice == 3:
    print(x, '*', y, '=', Multiply(x,y))
elif choice == 4:
    print(x, '/', y, '=', Divide(x,y)) 
else: 
    print("INVALID OPTION!.. ")