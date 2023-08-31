firstname = "John"
lastname = "Smith"
h = "hellohellohellohellohellohello_oooo"


print(firstname.upper())


print(firstname.lower())


print(firstname.__len__())


print(firstname.capitalize())


print(firstname.replace('h','_'))
print(firstname.replace('o',''))



print('_01_'.join(firstname))


print(firstname.split())
print(firstname.split('oh'))


print(h.count('hello')) # count times a substring or charcater appears in the string!
print(h.count('o'))


print(firstname.find('o')) # return index of character or first character of substring - if it exists: else returns -1 if substring not found
print(firstname.index('ohn')) # return index of character or first character of substring - if it exists: else returns an error message if substring not found
print(firstname.__contains__('hn')) # Returns true if substring exists, else false





'''
fn = ['J','o','h','n']
print(''.join(fn))
'''