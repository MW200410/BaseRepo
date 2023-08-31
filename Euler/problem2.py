listA = []
listb = []

def fib(n):
    a = 1 
    b = 2 
    sum = b
    listA.append(a)
    listA.append(b)
    listb.append(b)


    while b <= n: 
        temp = a
        a = b
        b = temp + b 
        listA.append(b)

        if b % 2 == 0: 
            sum += b
            listb.append(b)
            
    return sum

print(fib(4000000)) # Returns sum of even numbers in the fib sequence
print(listA) # lists the full sequence 
print(listb) # lists all even numbers in sequence