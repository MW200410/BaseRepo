'''
Collections are in-built data structures used to store and manipulate collections of items.

Commonly used Examples: 
list:  A dynamic array that can hold items of various data types
dictionary: A key-value pair where keys are unique and used to retrieve corresponding values.
tuples: An immutable sequence of items, used for grouping related data.
set: Collection of unique elements.

Others:
double ended queue
Counter
namedtuple

'''


# Lists - Can contain {objects, strings, int, float, nested lists, booleans}
# They are indexed


list_1 = ['J','o','h','n']
print(''.join(list_1))
print(type(''.join(list_1))) # Converts list to string

print(list_1[0])
print(list_1[0:3])


list_1.append('oo')
print(list_1)


list_1[4] = 'o'
print(list_1)


print(list_1.index('h'))


list_1.pop(1)
print(list_1)


list_1.insert(0,'w')
print(list_1)


list_1.sort() # Sorts list in alphabetical order! A-Z 
print(list_1)

# Dictionaries {Hash Maps}
# Dictionary keys will often be string values. Though they can be given various data types, as can values
# Dictionaries can contain dictionaries within them. 


contacts = {
    "jane": "07876434216"
}

print(type(contacts))
print(contacts['jane'])
print(contacts)

contacts['bob'] = "07876434218"
contacts['bill'] = "07876434259"
print(contacts,"\n")


print(contacts.keys())
print(contacts.values())

print(contacts.items())
print(list(contacts.items())[0])
print(list(contacts.items())[0][0])
print(list(contacts.items())[0][1])