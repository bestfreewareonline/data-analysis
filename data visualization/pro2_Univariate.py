import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column


pokemon = pd.read_csv('pokemon.csv')
#print(pokemon.columns)
'''
['id', 'species', 'generation_id', 'height', 'weight', 'base_experience', 'type_1', 
'type_2', 'hp', 'attack', 'defense', 'speed', 'special-attack', 'special-defense']
'''
'''
base_color = sb.color_palette()[0]  #each bar has the same color.
cat_order = pokemon['generation_id'].value_counts()
sb.countplot(data = pokemon, x = 'generation_id', color = base_color); #countplot for bar
plt.xticks(rotation = 90);

plt.show()


cat_order = pokemon['generation_id'].value_counts().sort_values(ascending=False)
cat_order.plot(kind = "bar",x = "id", y = "count")
plt.show()

'''

#gg = plt.hist(data = pokemon, x="speed", bins=20)
#print(gg)
'''
(array([  6.,  25.,  21.,  72.,  66.,  97.,  53., 106.,  64.,  64.,  69.,
        46.,  52.,  29.,  18.,   8.,   5.,   1.,   4.,   1.]), array([  5.  ,  12.75,  20.5 ,  28.25,  36.  ,  43.75,  51.5 ,  59.25,
        67.  ,  74.75,  82.5 ,  90.25,  98.  , 105.75, 113.5 , 121.25,
       129.  , 136.75, 144.5 , 152.25, 160.  ]), <a list of 20 Patch objects>)
    
'''

plt.hist(data = pokemon, x="speed", bins=40)
plt.show()
