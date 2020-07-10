import pandas as pd

patients = pd.read_csv("patients.csv")
treatments = pd.read_csv("treatments.csv")
adverse = pd.read_csv("adverse_reactions.csv")
nba = pd.read_csv("nba.csv")

pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)

'''
patients columns :  ['patient_id', 'assigned_sex', 'given_name', 
'surname', 'address', 'city', 'state', 'zip_code', 
'country', 'contact', 'birthdate', 'weight', 'height', 'bmi']
'''
#print("treatments columns : ", list(treatments))
'''
treatments columns :  ['given_name', 'surname', 'auralin',
'novodra', 'hba1c_start', 'hba1c_end', 'hba1c_change']
'''
#print("adverse columns : ", list(adverse))
'''
adverse columns :  ['given_name', 'surname', 'adverse_reaction']
'''

#print("nba columns : ", list(nba))
'''
nba columns :  ['Name', 'Team', 'Number',
'Position', 'Age', 'Height', 'Weight', 'College', 'Salary']
'''
inner_joined_total = patients.join(treatments.set_index(["surname"]),lsuffix="_x",rsuffix="_y",on=["surname"])#(503, 20)

inner_joined_total= patients.join(treatments, lsuffix="_left") #(503, 21)

inner_joined_total= patients.join(treatments, lsuffix="_right") #(503, 21)

inner_joined_total= nba.join(treatments, lsuffix="_right")#(458, 16) join to diffrent tables you can remove isuffix

print(inner_joined_total.shape)
print(list(inner_joined_total))