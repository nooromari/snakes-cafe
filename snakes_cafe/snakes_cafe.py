hello = """
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**                                  **
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
"""
print(hello)

num_order = []
user_order= ""
while user_order != "quit":
   user_order= input('> ')
   num_order.append(user_order)
   print()
   if user_order == "quit":
       break
   if num_order.count(user_order) > 1:
       order = 'orders'
   else :
       order = 'order'
   print(f"** {num_order.count(user_order)} {order} of {user_order} have been added to your meal **")
   print()