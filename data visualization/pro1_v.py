import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("athlete_events.csv")
new_df = df.dropna(subset= ["Medal"])

#print(new_df.columns)
'''
columns name
#['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 
# 'NOC', 'Games', 'Year', 'Season', 'City', 'Sport', 'Event', 'Medal']
'''

top_medals_by_age = new_df.groupby(["Age"])["Medal"].count().sort_values(ascending=False)
#print(top_medals_by_age)
'''
base_color = sb.color_palette()[0]
cat_order = new_df.groupby(["Age"])["Medal"].count().sort_values(ascending=False)
sb.countplot(data =new_df, x="Age", color=base_color);
plt.xticks(rotation=90);
plt.show()
'''

base_color = sb.color_palette()[0]
cat_order = new_df["Medal"].value_counts()
sb.countplot(data =new_df, x="Medal", color=base_color);
plt.xticks(rotation=90);
plt.show()