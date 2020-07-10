import pandas as pd

df = pd.read_csv("sales_data_types.csv")

pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column

print(df.dtypes)
'''
Customer Number    float64
Customer Name       object
2016                object
2017                object
Percent Growth      object
Jan Units           object
Month                int64
Day                  int64
Year                 int64
Active              object

...............................................
   Customer Number     Customer Name         2016          2017 Percent Growth Jan Units  Month  Day  Year Active
0          10002.0  Quest Industries  $125,000.00    $162500.00         30.00%       500      1   10  2015      Y
1         552278.0    Smith Plumbing  $920,000.00  $101,2000.00         10.00%       700      6   15  2014      Y
2          23477.0   ACME Industrial   $50,000.00     $62500.00         25.00%       125      3   29  2016      Y
3          24900.0        Brekke LTD  $350,000.00    $490000.00          4.00%        75     10   27  2015      Y
4         651029.0         Harbor Co   $15,000.00     $12750.00        -15.00%    Closed      2    2  2014      N

'''

df["Customer Number"] = df["Customer Number"].astype("int")

df["Percent Growth"] = df['Percent Growth'].apply(lambda x: x.replace('%', '')).astype('float') / 100

'''
def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)

df["2016"] = df["2016"].apply(convert_currency)
or the code below
'''
df["2016"] = df['2016'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')
df["2017"] = df['2017'].apply(lambda x: x.replace('$', '').replace(',', '')).astype('float')

df["Active"] = df["Active"].astype("bool")

# df["Active"] = np.where(df["Active"] == "Y", True, False)

df["Jan Units"] = pd.to_numeric(df['Jan Units'], errors='coerce').fillna(0)

#df['Month', 'Day', 'Year'] = pd.to_datetime(df[['Month', 'Day', 'Year']])

df["Month"] = pd.to_datetime(df['Month'])
df["Day"] = pd.to_datetime(df['Day'])
df["Year"] = pd.to_datetime(df['Year'])

#df['Customer Name'] = df['Customer Name'].astype(str)    objyct type = str type

print((df.head()))
print(df.dtypes)
'''
Customer Number             int32
Customer Name              object
2016                      float64
2017                      float64
Percent Growth            float64
Jan Units                 float64
Month              datetime64[ns]
Day                datetime64[ns]
Year               datetime64[ns]
Active                       bool
'''
