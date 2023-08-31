'''
Do not work on string data types. Can be used to evaluate the length of a string since the output of the function len() is an int. 
'''

print("EQUAL TO/NOT EQUAL TO:-")

# Equal To? (==)
print("Is it True that 4 is equal to 3? ",4==3, "   |  ", "Is True that 4 is equal to 4? ", 4==4)

# Not Equal To? (!=)
print("Is it TRUE that 4 is not equal to 3? ",4!=3, "   |  ", "Is it True that 4 is not equal to 4? ", 4!=4,"\n") 



print("MORE THAN/MORE THAN OR EQUAL TO:-")
# Greater than? (>)
print("Is it TRUE that 4 is greater than 3? ",4>3, "   |  ", "Is it True that 4 is greater than 4? ", 4>4) 

# Greater than or equal to? (>=)
print("Is it TRUE that 4 is greater than or equal to 3? ",4>=3, "   |  ", "Is it True that 4 is greater than or equal to 4? ", 4>=4,"\n") 



print("LESS THAN/LESS THAN OR EQUAL TO:-")
# Less than? (<)
print("Is it TRUE that 4 is less than 3? ",4<3, "   |  ", "Is it True that 4 is less than 4? ", 4<4) 

# Less than or equal to? (<=)
print("Is it TRUE that 4 is less than or equal to 3? ",4<=3, "   |  ", "Is it True that 4 is less than or equal to 4? ", 4<=4, "\n")


# Truthy vs Falsey
print("Anything that is not zero returns true (1,-1,-2, 2):",bool(1), bool(-1), bool(-2), bool(2))
print("Zero Returns False (0):",bool(0))
print("Empty strings also return false: ",bool(""))

