# %%

from datasci import datasci
import pandas as pd


df = pd.read_csv("flights_december.csv")
m = datasci(df)
print(df.head())

#%%

# print(m.size())
print(m.missingReport())

# df.to_csv("flights_december.csv", index=False)
# df.drop(['Unnamed: 0'], axis=1, inplace=True)
# print(df.head())
# print(df.shape)

# %%
m.imputation(columns=['TAXI_IN','ARRIVAL_TIME'], impute='other', check=True)


# %%
print(df['AIRLINE'].value_counts())

#%%
old = ['AA','DL']
new = ['American Airline','Delta']

m.recode(column = 'AIRLINE', oldVal=old, newVal=new, inplace=True)


# %%
