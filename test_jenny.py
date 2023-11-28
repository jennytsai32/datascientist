# %%

from datasci import datasci
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


df = pd.read_csv("flights_december.csv")
m = datasci(df)
print(df.head())

#%%

# print(m.size())
print(m.missingReport(insight=True))

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


#%%
print(df.dtypes)

# %%
print(m.eda('TAXI_IN'))


# %%
print(m.eda('AIRLINE'))


# %%
# num of missing
# max, min, mean, median, sd
# correlation with target variable

# If skewness is between -0.5 and 0.5, the distribution is approximately symmetric.







# %%
