print("Q1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]



# A1a: 
print(x[0:5])



print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for i in x: 
    if i % 2 == 0: 
        print(i)



print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for idx, i in enumerate(x):
    if i % 2 == 0 and idx < 5:
        print(f"Element: {idx+1}, Is the even number: {i}")
      

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
list_1 = []

for i in names: 
    list_1.append(i[0])
print(list_1)




print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
list_2 = []
for i in names: 
    list_2.append(i.index(" "))

print(list_2)



print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
list_3 = []

for i in names: 
    list_3.append(i[0]+""+i[i.index(" ")+1])
print(list_3)




# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]




# A3a:

for i in list_of_lists:
    if len(set(i)) == len(i): 
        print(f"{i}:  has no duplicates")


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

Ask = int(input("Please input a number greater than 100: "))
while Ask <= 100:
    Ask = int(input("Too low please input a number greater than 100: "))
print("You entered:", Ask)


# A4a:


print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:



Q = int(input("Please input a number greater than 100: "))

while Q <= 100:
    Q = int(input("Too low please input a number greater than 100: "))


if Q == 0 or Q ==1:
    print("not prime") 
for i in range(2,Q-1):
      if Q % i == 0: 
           print("not prime")
           break
else: 
     print("prime")
    

