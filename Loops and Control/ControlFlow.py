'''
Example: Managing film certification details 
'''

customer_age = 18



if customer_age < 12: 
    print("U, PG movies available")
elif customer_age < 15: 
    print("U, PG, 12 rated movies available")
elif customer_age < 18:
    print("U, PG, 12, 15 rated movies avialable")
else:
    print("All movies available") 


TimeOfDay = 24


if TimeOfDay < 5 and TimeOfDay > 0: 
    print("Good Morning!")
elif TimeOfDay >= 5 and TimeOfDay < 12: 
    print("Good Morning!")
elif TimeOfDay == 12: 
    print("Noon")
elif TimeOfDay < 17 and TimeOfDay > 12: 
    print("Good Afternoon!")
elif TimeOfDay < 24 and TimeOfDay >= 17: 
    print("Good Evening!")
elif TimeOfDay == 24 or TimeOfDay == 0:
    print("Midnight")


