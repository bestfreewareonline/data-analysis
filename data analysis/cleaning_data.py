import numpy as np
import pandas as pd

patients = pd.read_csv("patients.csv")
treatments = pd.read_csv("treatments.csv")
adverse_reactions = pd.read_csv("adverse_reactions.csv")
treatments_cut = pd.read_csv("treatments_cut.csv")


#pd.set_option('display.max_rows', 500)  # to show all rows change the number 100
pd.set_option('display.max_column', 100)  # to show all column


pd.set_option("display.width", 1000)
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    #print(patients) # to show all rows

# 1- Assessing
#print(patients)
#print(adverse_reactions.head())
#print(patients.info())
#print(adverse_reactions.describe())
#print(patients["weight"].sort_values())
#print(patients[patients["surname"].duplicated()])
#print(patients["surname"].value_counts())
#patients[patients['address'].isnull()]

#all_columns = pd.Series(list(patients) + list(treatments) + list(adverse_reactions))
#print(all_columns[all_columns.duplicated()])
'''
output
14    given_name
15       surname
21    given_name
22       surname
'''

# 2- Cleaning data

patients_clean = patients.copy()
treatments_clean = treatments.copy()
adverse_reactions_clean = adverse_reactions.copy()

# In patients table, 'Contact' column should be split into 'phone_number' and 'email'.

patients_clean['phone_number'] = patients_clean.contact.str.extract('((?:\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})', expand=True)

#print(patients_clean['phone_number'].head(3))

patients_clean['email'] = patients_clean.contact.str.extract('([a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+[a-zA-Z])', expand=True)

#print(patients_clean['email'].sample(3))


# Drop the original
patients_clean = patients_clean.drop('contact', axis=1)

treatments_clean = pd.melt(treatments_clean,
                           id_vars=['given_name', 'surname', 'hba1c_start', 'hba1c_end', 'hba1c_change'],
                           var_name='treatment', value_name='dose')

treatments_clean = treatments_clean[treatments_clean.dose != "-"]
treatments_clean['dose_start'], treatments_clean['dose_end'] = treatments_clean['dose'].str.split(' - ', 1).str
treatments_clean = treatments_clean.drop('dose', axis=1)

#print(treatments.head(2))
#output    ['given_name', 'surname', 'auralin', 'novodra', 'hba1c_start', 'hba1c_end', 'hba1c_change']
#print(treatments_clean.head(3))
#output   given_name     surname  hba1c_start  hba1c_end  hba1c_change treatment dose_start dose_end

# Adverse reaction table should be part of the treatments table
treatments_clean = pd.merge(treatments_clean, adverse_reactions_clean, on=['given_name', 'surname'], how='left')

# In patients, treatments and adverse_reactions tables, 'Given name' and 'surname' columns are duplicated.

id_names = patients_clean[['patient_id', 'given_name', 'surname']]
id_names.given_name = id_names.given_name.str.lower()
id_names.surname = id_names.surname.str.lower()

treatments_clean = pd.merge(treatments_clean, id_names, on=['given_name', 'surname'])
treatments_clean = treatments_clean.drop(['given_name', 'surname'], axis=1)

#test to see duplicated columns in all tables   should patient_id only
#all_columns = pd.Series(list(patients_clean) + list(treatments_clean))
#print(all_columns[all_columns.duplicated()])


# in 'treatments' dataset: "Missing records (280 instead of 350)

treatments_clean = pd.concat([treatments_clean, treatments_cut], ignore_index=True)

# in 'treatments' dataset: "Inaccurate HbA1c changes"

treatments_clean.hba1c_change = (treatments_clean.hba1c_start - treatments_clean.hba1c_end)

#print(treatments_clean.hba1c_change.head())

# Fixing datatype
#  in 'patients' dataset: Zip code is a float and Zip code has four digits sometimes
patients_clean.zip_code = patients_clean.zip_code.astype(str).str[:-2].str.pad(5, fillchar='0')

# Reconvert NaNs entries that were converted to '0000n' by code above
patients_clean.zip_code = patients_clean.zip_code.replace('0000n', np.nan)


patients_clean.assigned_sex = patients_clean.assigned_sex.astype('category')
patients_clean.state = patients_clean.state.astype('category')
patients_clean.birthdate = pd.to_datetime(patients_clean.birthdate)

#treatments_clean.dose_start = treatments_clean.dose_start.str.strip('u').astype(int)
#treatments_clean.dose_end = treatments_clean.dose_end.str.strip('u').astype(int)
#print(treatments_clean.info())









