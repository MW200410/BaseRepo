print("Q1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:

def Factors(n):
    l1 =[]
    for i in range(1,n+1):
        if n%i==0:
            l1.append(i)
    print(l1)
    #l1.clear()
        
Factors(12)



print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def Factors2(a, b):
        if a%b==0 or b%a ==0:
            return True
        else:
            return False
        
print(Factors2(12,6))
print(Factors2(15,3))






# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


def LocInAlphabet(string):
     Alph_loc = alphabet.index(string) + 1 
     Alph_loc = str(Alph_loc)

     if int(Alph_loc[-1]) == 1:
        print(f"{Alph_loc}st letter in the alphabet")
     elif int(Alph_loc[-1]) == 2: 
          print(f"{Alph_loc}nd letter in the alphabet")
     elif int(Alph_loc[-1]) == 3: 
          print(f"{Alph_loc}rd letter in the alphabet")
     elif int(Alph_loc) >= 4 and int(Alph_loc) <=20 or int(Alph_loc) >= 24 and int(Alph_loc) <= 26: 
          print(f"{Alph_loc}th letter in the alphabet")
     #print(Alph_loc)
     
LocInAlphabet("a")
     
     


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def name_to_ID(name):
    ID = ""
    for char in name: 
         ID += str(alphabet.index(char))
    return ID
         

print(name_to_ID("bob"))



print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def ID_to_Password(ID):
    val = 0 
    ID_Number = int(ID)
    for i in ID: 
         val += int(i)
    return ID_Number-val
    
print(ID_to_Password(name_to_ID("bob")))


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def A_Prime(n):
     if n == 0 or n ==1:
          return False 
     for i in range(2,n-1):
          if n % i == 0: 
               return False 
     else: 
          return True 

print(A_Prime(104))
               



print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def A_Prime2(CheckPrime):
     n = int(CheckPrime)
     if n == 0 or n ==1:
          return False 
     for i in range(2,n-1):
          if n % i == 0: 
               return False 
     else: 
          return True 

print(A_Prime2('7'))


# -------------------------------------------------------------------------------------- #
