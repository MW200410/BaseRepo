class Table():
    def __init__(self, table_size):
        self.table_size = table_size
        self.bill = []

    
    def order(self, item, price, quantity=1):
        dict = {'item':'',
                'price':'',
                'quantity':''}
        dict['item'] = item
        dict['price'] = price 
        dict['quantity'] = quantity



        if len(self.bill) < 1: 
            self.bill.append(dict)
            return
        
        if len(self.bill) >= 1: 
            for i in self.bill: 
                    if i['item'] == item and i['price'] == price:
                        i['quantity'] += quantity
                        return 
                        #print('hello')
                    elif i['item'] != item or i['price'] != price:
                        self.bill.append(dict)
                        return 
                    
    def remove(self, item, price, quantity=1):
        for i in self.bill: 
                if i['item'] == item and i['price'] == price:
                    if i['quantity'] >= quantity: 
                            if i['quantity'] == 1: 
                                 print('removing final value')
                                 self.bill.remove(i)
                            else:
                                i['quantity'] -= quantity
                            return True
                    else:    
                        print('Cannot remove more items than ordered')
                        return False           
        print('item/price difference')    
        return False
                    

    def get_subtotal(self):
        total = 0
        for i in self.bill:
            x = list(i.values())
            total += x[1]*x[2]
        return total 
    
    
    def get_total(self, service_charge=0.10): 
        self.service_charge = service_charge

        dic = {'Sub Total':'',
               'Service Charge':'',
               'Total':''}
        
        t = self.get_subtotal()
       
        dic['Total'] = f"£{t + t*service_charge:.2f}"
        dic['Service Charge'] = f"£{t + t*service_charge - t:.2f}"
        dic['Sub Total'] = f"£{t:.2f}"

        return dic 
    
    
    def split_bill(self):
        return round(self.get_subtotal()/self.table_size, 2)

        

        # should represent a table at a restaurant 
        


t = Table(5)
#print(t.bill)
#t.order('apple', 2,1)
#print(t.bill)
#t.order('apple', 5)
#print(t.bill)
#t.order('pear', 12)
#print(t.bill)




t.order('peaach', 10,12)
print(t.bill)
print(t.get_total())

'''
print('\n')

t.get_subtotal()
print(t.get_total(0.1))

print(t.split_bill())
'''

'''

print(t.remove('pear', 12, 1))
print(t.bill)
print(t.remove('pear', 12, 3))
print(t.bill)
'''
#print(t.remove('pear',14))
#print(t.remove('pear',14, 2))

#print(t.remove('apple', 5))
#print(t.bill)
#t.remove('apple', 5)
#print(t.bill)


'''
#t.order('apple', 5)
print(t.bill)
t.order('apple', 5)
print(t.bill)
t.order('apple', 6)
print(t.bill)
t.order('pear', 12)
print(t.bill)
t.order('plum', 50)
print(t.bill)
'''