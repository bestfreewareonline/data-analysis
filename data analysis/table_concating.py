import pandas as pd

patients = pd.read_csv("patients.csv")
treatments = pd.read_csv("treatments.csv")
adverse = pd.read_csv("adverse_reactions.csv")
nba = pd.read_csv("nba.csv")

pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)

print("patients columns : ", list(patients))
'''
patients columns :  ['patient_id', 'assigned_sex', 'given_name', 
'surname', 'address', 'city', 'state', 'zip_code', 
'country', 'contact', 'birthdate', 'weight', 'height', 'bmi']
'''
print("treatments columns : ", list(treatments))
'''
treatments columns :  ['given_name', 'surname', 'auralin',
'novodra', 'hba1c_start', 'hba1c_end', 'hba1c_change']
'''
print("adverse columns : ", list(adverse))
'''
adverse columns :  ['given_name', 'surname', 'adverse_reaction']
'''

print("nba columns : ", list(nba))
'''
nba columns :  ['Name', 'Team', 'Number',
'Position', 'Age', 'Height', 'Weight', 'College', 'Salary']
'''

double_precip = pd.concat([patients, treatments])  #(783, 19)

reindexed = pd.concat([patients, treatments], ignore_index=True) #(783, 19)

inner_joined_cols = pd.concat([patients, treatments], axis=1, join="inner") #(280, 21)

inner_joined_cols = pd.concat([patients, treatments], axis=0, join="inner") # (783, 2) , ['given_name', 'surname']

inner_joined_cols = pd.concat([patients, treatments], axis=1, join="outer") #(503, 21)

hierarchical_keys = pd.concat([patients, treatments], keys=['patient_id', 'given_name']) #(783, 19)

appended = patients.append(nba) #(961, 23)


double_precip = pd.concat([nba, treatments]) #(738, 16)


print(appended.shape)
print(list(appended))
print(hierarchical_keys.head())