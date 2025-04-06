import pandas as pd


df=pd.read_csv('Pandas/Employers.csv')
searcName=df.loc[df['First Name']=='Sara'],['First Name','Last Name']
print(searcName.count)