import pandas as pd

data = pd.read_csv("nba.csv")
orders = pd.read_excel("orders.xlsx")

pd.set_option('display.max_rows', 6000)
pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column

print((data.head()))

'''
            Name            Team  Number Position   Age Height  Weight            College     Salary
0  Avery Bradley  Boston Celtics     0.0       PG  25.0    6-2   180.0              Texas  7730337.0
1    Jae Crowder  Boston Celtics    99.0       SF  25.0    6-6   235.0          Marquette  6796117.0
'''

# new data frame with split value columns
new = data["Name"].str.split(" ", n=1, expand=True)


# making separate first name column from new data frame
data["First Name"] = new[0]

# making separate last name column from new data frame
data["Last Name"] = new[1]

#print(data.head())

'''
   First  Name Last 
0  Avery  Bradley
1  Jae    Crowder
2  John   Holland
3  R.J.   Hunter
4  Jonas   Jerebko
'''

#data.drop(columns =["Name"], inplace = True)

# new data frame with split value columns
height = data["Height"].str.split("-", n=1, expand=True)

# making separate first name column from new data frame
data["max"] = height[0]

# making separate last name column from new data frame
data["min"] = height[1]
'''

#print(data.head())

''
    max    min
0    6      2
1    6      6
2    6      5
'''

# new data frame with split value columns
position = data["Position"].str.split("", n=0, expand=True)

# making separate first name column from new data frame
data["first"] = position[1]

# making separate last name column from new data frame
data["last"] = position[2]

#print(data.head())
'''
   first   last
0  P        G
1  S        F
'''

# new data frame with split value columns
data["Number"] = data["Number"].astype(str)

data["col1"] = data["Number"].str[0:2]
data["col2"] = data["Number"].str[2:4]

#print(data.head())

df = orders["Order Date"].dt.hour.head()
orders["Day"] = orders["Order Date"].dt.day.head()
orders["Month"] = orders["Order Date"].dt.month.head()
orders["Year"] = orders["Order Date"].dt.year.head()

#data["Height"] = data["Height"].str.replace('-','  ') # to remove - mark
#print(orders.head())