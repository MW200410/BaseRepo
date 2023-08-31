'''
What a python interpreter sees when reading a string is a group of unicode characters: 
'''

# unicode to char
print(U'\u0061')


# String Basics 
my_string = "Hello world"

# 1 Returning a character from a string using the index
print("First Character: ",my_string[0])
print("Last Character: ",my_string[-1])

print("Range of Characters A: ",my_string[:5]) # everything up to (5-1) from 0. 
print("Range of Characters B: ",my_string[-5:])  # -5 and everything after 
print("Range of Characters C: ",my_string[-5:-1])  # This time does not print -1 -> (d).  Instead the character beforehand -> (l)


# Concatenation and escape characters 

s1 = 'jane'
s2 = 'doe'
age = 25 


# Concatenate Example 1
s3 = s1 +" "+ s2
print(s3)

# Concatenate Example 2 
print(s3+" "+str(age)) # cast int 'age' to string so to concatenate


# Escape characters - Used when we have double quotes that appear within a string that is itself contained by double quotes.
s = "Jane said: \"Hello World\" " 
print(s) 










