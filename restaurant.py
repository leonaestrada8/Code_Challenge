# Checkpoint 1 

'''
Checkpoint 1: The tables dictionary is created and initialized with seven keys, each representing a table, 
and their values are dictionaries with keys for 'name', 'vip_status', and 'order'. Some of the tables are empty dictionaries ({}).

'''

tables = {
    1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


'''Checkpoint 2: The assign_table function is defined. This function takes in three arguments: 
table_number, name, and vip_status with a default value of False. It updates the values of 'name', 'vip_status', and 'order' 
for the specified table number in the tables dictionary.

'''

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

# Checkpoint 2

'''Checkpoint 3: The assign_and_print_order function is defined. 
This function takes in two arguments: table_number and *order_items (a variable number of order items represented as a tuple). 
It updates the 'order' for the specified table number with the order_items tuple.
'''

def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for order_item in order_items:
        print(order_item)

#Checkpoint 4: The function then iterates over each order_item in the order_items tuple and prints each item.

# Checkpoint 5
'''Checkpoint 5: The assign_table function is called with 2 as the table number, 'Arwa' as the name, and True as the vip_status. This updates the values of 'name', 'vip_status', and 'order' for table 2 in the tables dictionary.

'''
assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

# Checkpoint 6
'''Checkpoint 6: The assign_and_print_order function is called with 2 as the table number
and 'Steak', 'Seabass', and 'Wine Bottle' as the order_items. 
This updates the 'order' for table 2 in the tables dictionary with the order_items tuple and prints each order_item.
'''

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks
  
  
  assign_food_items(2, food = 'Seabass, Gnocchi, Pizza', drinks = 'Margarita, Water')


def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(f"Appetizer: {appetizer}")
    print("Entrees:")
    for entree in entrees:
        print(f"  {entree}")
    print(f"Sides: {sides}")
    print("Dessert Scoops:")
    for flavor, quantity in dessert_scoops.items():
        print(f"  {flavor}: {quantity} scoop(s)")


single_prix_fixe_order('Caesar salad', 'Steak', 'Grilled salmon', sides='Roasted vegetables', vanilla=3, chocolate=1)

def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  print(f"total tip: {total_tip}")
  split_price = (total + total_tip) / split
  print(split_price)


table_7_total = [534.50, 20.0, 5]


print(calculate_price_per_person(*table_7_total))
