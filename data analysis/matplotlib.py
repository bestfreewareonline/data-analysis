import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


orders = pd.read_excel("orders.xlsx")
people = pd.read_excel("people.xlsx")
returns = pd.read_excel("returns.xlsx")


products_by_coustomer = orders.groupby("Customer Name")["Product Name"]

print(products_by_coustomer)
plt.show()
