#!/usr/bin/env python
# coding: utf-8

# In[14]:


menu={
    'pizza': 100,
    'pasta': 70,
    'burger': 90,
    'salad': 60,
    'fries':90,
    'coffee':70,

    
}

print("welcome to mehak ka restaurant")
print("menu")
print("pizza: rs 100\npasta: rs70,\nburger:rs90\nsalad:rs60\nfries:rs90\ncoffee:rs70")


order_total=0

item_1=input("enter the name of item of item you want to add in your cart= ")
if item_1 in menu:
    order_total +=menu[item_1]
    print(f"order item {item_1} has been added to your cart")
    
else: 
    print(f"entered item{item_1} is not available at our outlet yet:( ")
    
another_order = input("do you want to add something else? (yes/no)")

if another_order=="yes":
    item_2= input(" enter the name of your item to cart: ")
    if item_2 in menu: 
        order_total +=menu[item_2]
        print(f"item{item_2} has been added to your cart")
        
    else:
        print(f"ordered item {item_2} is not available :( ")
        
        
print(f" the total amount you need to pay is {order_total}")
        


# In[ ]:





# In[ ]:




