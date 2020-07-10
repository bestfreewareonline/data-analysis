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
columns name
#['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 
# 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal']
'''


df = fuel_econ.copy()
'''
df['VClass'] = df['VClass'].astype('category')
g = sb.FacetGrid(data = df, col = 'VClass', height = 3, col_wrap = 5)
g.map(plt.scatter, 'city', 'highway', alpha = 0.2)
plt.show()
'''
'''
df_sub = df[df['fuelType'].isin(['Premium Gasoline', 'Regular Gasoline'])]
g = sb.FacetGrid(data = df_sub, col = 'VClass',height = 3, col_wrap = 5)
g.map(sb.boxplot, 'fuelType', 'displ')
plt.show()

'''
'''
df_sub = df[df['fuelType'].isin(['Premium Gasoline', 'Regular Gasoline'])]
sb.boxplot(data = df_sub, x = 'VClass', y = 'displ', hue = 'fuelType')
plt.legend(loc = 6, bbox_to_anchor = (1.0, 0.5)) # legend to right of figure
plt.xticks(rotation = 15)
plt.show()
'''
'''
group_order = df.make.value_counts().index

g = sb.FacetGrid(data = df, col = 'make', col_wrap = 6, height = 2, col_order = group_order)
g.map(plt.hist, 'comb', bins = np.arange(df.comb.min(), df.comb.max(), 2))
g.set_titles('{col_name}')
plt.show()
'''
mean_comb = df.groupby('make').mean()
order =  mean_comb.sort_values('comb', ascending = False).index
base_color = sb.color_palette()[0]
ax= sb.barplot(data = df,x = 'make', y = 'comb', color = base_color, ci = 'sd', order = order)
ax.legend(loc = 1, framealpha = 1) #graph frame
plt.xticks(rotation = 45) #graph frame
plt.show()
