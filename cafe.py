# Create a list menu with the items my cafe is going to sell. 
# The requirement was to make a list of at least 4 items.
# The items for sale are: 'Soup', 'Hot choclate', 'Mineral water' and 
# 'Cake'.

menu_list = ['Soup', 'Hot chocolate', 'Mineral water', 'Cake']
print(menu_list)


# Create a dictionary called stock, which contains the stock value for 
# each item on the cafe's menu.
# In my case, I have in stock 20 jars of 'Soup', 65 times 250g 
# containers of 'Hot chocolate', 100 times 500ml of 'Mineral water'(still 
# water) and 20 "Victoria Sponge Cakes".
stock_dict = { 'Soup': 20,
               'Hot chocolate': 65,
               'Mineral water': 100,
               'Cake': 20
             }

stock_list = [('Soup', 20), ('Hot chocolate', 65), ('Mineral water', 
100), ('Cake', 20)]
stock_dict = (dict(stock_list))
print(stock_dict)

# Create another dictionary called price, which contains the prices for 
# each item on my cafe's menu.
# The items as listed are: a bowl of 'Soup' costs £7.70, a cup of a 'Hot 
# chocolate' costs £3.20, a 500ml bottle of still 'Mineral water' costs £2.80
# and a slice of a "Victoria sponge" cake costs £3.80.
price_dict = { 'Soup': 7.70,
               'Hot chocolate': 3.20,
               'Mineral water': 2.80,
               'Cake': 3.80
             }
print(price_dict)


# a new variable introduced total_stock to store the total stock worth
total_stock =  0


# loop through the 'menu list':
for item in menu_list:
     # calculate each 'item value' by multiplying the 'stock value' by 
     # the 'price value':
     total_stock += float(stock_dict[item]) * float(price_dict[item])
# The total price of the total stock is 718. It is £718 as all the listings 
# are valued in pounds. Prints 718.0
print(total_stock) 





