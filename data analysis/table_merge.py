import pandas as pd

patients = pd.read_csv("patients.csv")
treatments = pd.read_csv("treatments.csv")
adverse = pd.read_csv("adverse_reactions.csv")
nba = pd.read_csv("nba.csv")


pd.set_option('display.max_column', 100)  # to show all column
pd.set_option("display.width", 1000)   # to show all column

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

# merge

show_row = patients[patients["surname"] == "Phan"]
inner_merged = pd.merge(show_row, patients)
print(inner_merged.head())

print(patients.shape) # (503, 14)
print(treatments.shape) # (280, 7)

inner_merged_total = pd.merge(patients, treatments, how="inner", on=["given_name", 'surname']) # (0, 19)

inner_merged_total = pd.merge(patients, treatments, how="outer", on=["given_name", 'surname']) # (783, 19)

inner_merged_total = pd.merge(patients, treatments, how="left", on=["given_name", 'surname']) # (503, 19)

inner_merged_total = pd.merge(patients, treatments, how="right", on=["given_name", 'surname']) # (280, 19)


print(inner_merged_total.head())
print(inner_merged_total.shape)

