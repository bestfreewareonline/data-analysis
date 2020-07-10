import pandas as pd


nba= pd.read_csv("nba.csv")
people = pd.read_excel("people.xlsx")
returns = pd.read_excel("returns.xlsx")


pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column


'''
nba = ['Name', 'Team', 'Number', 'Position', 'Age', 'Height', 'Weight', 'College', 'Salary']
people =  ['Person', 'Region']
returns = ['Returned', 'Order ID', 'Market']
'''

frames = returns[['Market']]
data = people['Region']
free = nba['Name'], nba['Team']
new_data = frames.join(data)
last_data = new_data.join(free)
new_table = last_data.to_csv("new_table.csv")
df = pd.read_csv("new_table.csv")
print(df.head())

#precip_one_station = climate_precip[climate_precip["STATION"] == "GHCND:USC00045721"]















