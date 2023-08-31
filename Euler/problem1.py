# Find the sum of all the multiples of 3 and 5 below 1000. 
import numpy as np 

listA = []

for i in range(1,400):
    if 3*i < 1000:
        listA.append(3*i)
    if 5*i < 1000:
        listA.append(5*i)

the_set = set(listA)

print(sum(the_set))

# Ans 233,168
