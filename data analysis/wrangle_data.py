import numpy as np
import pandas as pd



orders = pd.read_excel("orders.xlsx")
people = pd.read_excel("people.xlsx")
returns = pd.read_excel("returns.xlsx")

pd.set_option('display.max_rows', 6000)
pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column

#print(orders.info())
#print(people.info())
#print(returns.info())
'''
 #   Column          Non-Null Count  Dtype         
---  ------          --------------  -----         
 0   Row ID          51290 non-null  int64         
 1   Order ID        51290 non-null  object        
 2   Order Date      51290 non-null  datetime64[ns]
 3   Ship Date       51290 non-null  datetime64[ns]
 4   Ship Mode       51290 non-null  object 
'''


print(orders.head())
#print(people.head())
#print(returns.head())

# questions & answers
#  avg for quantity $ discount & shipping cost and profit
print(orders.describe())

'''
    Row ID   Postal Code         Sales      Quantity      Discount        Profit  Shipping Cost
count  51290.00000   9994.000000  51290.000000  51290.000000  51290.000000  51290.000000   51290.000000
mean   25645.50000  55190.379428    246.490581      3.476545      0.142908     28.610982      26.375818
std    14806.29199  32063.693350    487.565361      2.278766      0.212280    174.340972      57.296810
min        1.00000   1040.000000      0.444000      1.000000      0.000000  -6599.978000       0.002000
25%    12823.25000  23223.000000     30.758625      2.000000      0.000000      0.000000       2.610000
50%    25645.50000  56430.500000     85.053000      3.000000      0.000000      9.240000       7.790000
75%    38467.75000  90008.000000    251.053200      5.000000      0.200000     36.810000      24.450000
max    51290.00000  99301.000000  22638.480000     14.000000      0.850000   8399.976000     933.570000
'''

#orders columns
print(list(orders))
'''
['Row ID', 'Order ID', 'Order Date', 'Ship Date',
 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'City', 'State',
  'Country', 'Postal Code', 'Market', 'Region', 'Product ID', 'Category', 
  'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit',
   'Shipping Cost', 'Order Priority']

'''
# 2- unique for customer name, customer id
print(orders['Customer Name'], orders['Customer ID'].unique())
'''
0             Rick Hansen
1           Justin Ritter
2            Craig Reiter
'''

# 3- max an min for ship mode & city & state & product name & category & market  customer name

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    ship_mode = (orders["Ship Mode"].value_counts())

    city = (orders["City"].value_counts())

    state = (orders["State"].value_counts())

    product_name = (orders["Product Name"].value_counts())

    category = (orders["Category"].value_counts())

    market = (orders["Market"].value_counts())

    coustmer_name = (orders["Customer Name"].value_counts())


#print(product_name, city,ship_mode, state,category,market)
print(state)
'''
California                              2001
England                                 1499
New York                                1128
Texas                                    985
'''


all_columns = pd.Series(list(orders) + list(people) + list(returns))
print(all_columns[all_columns.duplicated()])

#Region, Order ID, Market

#print(orders["Customer Name", input("Muhammed Yedwab")])

#customer_product = orders[(orders['Customer Name'] == " Rick Hansen") == (orders['Product Name'] == "Motorola Smart Phone")]

#print(customer_product)
#print(orders['Product Name'].head())


#

with pd.option_context('display.max_rows', None, 'display.max_columns', None):


 products_by_coustomer = orders.groupby("Customer Name")["Product Name"].max()


 products_by_coustomer = orders.groupby("Customer Name")["Product Name"].sum()


 products_by_coustomer = orders.groupby("Customer Name")["Product Name"].count()


 coustomer_by_quantity = orders.groupby(["Customer Name", "Product Name "])["Quantity"].count()


 coustomer_by_profit = orders.groupby(["Customer Name"])["Profit"].count()


 most_quantity = orders.groupby(["Customer Name"]).sum().sort_values("Quantity", ascending=False)


 most_sales = orders.groupby(["Customer Name", "Country"]).sum().sort_values("Sales", ascending=False)


 most_sales = orders.groupby(["Market", "State"]).sum().sort_values("Sales", ascending=False)


 specific_user = orders[orders['Customer Name'] == 'Bill Eplett'].groupby('Product Name').sum()


 specific_user = orders[orders['Customer Name'] == 'Bill Eplett'].groupby('Country').sum()


 precip_one_station = orders[orders["Customer Name"] == "Muhammed Yedwab"]


 orders_by_customer = orders[orders["Customer Name"] == "Muhammed Yedwab"].sum()

print(orders_by_customer)
''
#most_quantity
''''                    Row ID  Postal Code        Sales  Quantity  Discount      Profit  Shipping Cost
Customer Name                                                                                           
Bill Eplett             1920288     369095.0  28479.16740       411     8.522  7410.00530     2695.77400
Eric Murdock            2284783     356266.0  28084.40348       392    15.344  3306.01548     3127.88800
Steven Ward             2264257     256284.0  25668.48600       383    10.340  2794.73160     2363.26000
''



'''
#id_names = patients_clean[['patient_id', 'given_name', 'surname']]
#id_names.given_name = id_names.given_name.str.lower()
#patients_clean = patients.copy()
#patients_clean = patients_clean.drop('contact', axis=1)











