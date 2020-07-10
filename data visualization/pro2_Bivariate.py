import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


pd.set_option('display.max_rows', 6000)
pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column

fuel_econ = pd.read_csv('fuel_econ.csv')

#print(fuel_econ.columns)

'''
['id', 'make', 'model', 'year', 'VClass', 'drive', 'trans', 'fuelType', 'cylinders', 'displ', 'pv2', 'pv4', 
'city', 'UCity', 'highway', 'UHighway', 'comb', 'co2', 'feScore', 'ghgScore']
'''
'''
df = fuel_econ.copy()
df = df.query('fuelType == "Regular Gasoline" or fuelType == "Premium Gasoline"')
ax = sb.countplot(data = df, x = 'VClass', hue = 'fuelType')
ax.legend(loc = 1, framealpha = 1)
plt.xticks(rotation = 45)
plt.show()
'''
'''
df = fuel_econ.copy()
df = df.query('year == "2013" or year == "2018"')#for first column we need to graph
ax = sb.countplot(data = df, x = 'fuelType', hue = 'year') #second column
ax.legend(loc = 1, framealpha = 1) #graph frame
plt.xticks(rotation = 45) #graph frame
plt.show()
'''
'''
df = fuel_econ.copy()
group_order = df.make.value_counts().index

g = sb.FacetGrid(data = df, col = 'make', col_wrap = 6, height = 2, col_order = group_order)
g.map(plt.hist, 'comb', bins = np.arange(df.comb.min(), df.comb.max(), 2))
g.set_titles('{col_name}')
plt.show()

'''
'''
# bins_x = np.arange(0.5, 10.5+1, 1)
# bins_y = np.arange(-0.5, 10.5+1, 1)
# bins = [bins_x, bins_y],
plt.hist2d(data = fuel_econ, x = 'displ' , y = 'co2', cmap = 'viridis_r', cmin = 0.5)
plt.colorbar()
plt.show()
'''
'''
df = fuel_econ.copy()
mean_comb = df.groupby('make').mean()
order =  mean_comb.sort_values('comb', ascending = False).index
base_color = sb.color_palette()[0]
sb.barplot(data = df, x = 'comb', y = 'make', color = base_color, ci = 'sd', order = order)
plt.show()
'''
'''
base_color = sb.color_palette()[0]
sb.violinplot(data = fuel_econ, x = 'VClass', y = 'displ', color = base_color,
              inner = 'quartile')
plt.xticks(rotation = 30)
plt.show()
'''