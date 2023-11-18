# %%

import datasci as ds
import pandas as pd


df = pd.read_csv("flights_december.csv")

#df.to_csv("flights_december.csv", index=False)
#print(df.head())
print(df.shape)

# %%

#print(df.columns[df.isnull().any()].tolist())
missingVal = df[df.columns[df.isnull().any()].tolist()].isnull().sum()
print(missingVal)
print(len(missingVal))

# %%
missingPer = round((df[df.columns[df.isnull().any()].tolist()].isnull().sum() * 100/ len(df)),2)
print(missingPer)
print(len(missingPer))

# %%
frame = {'Num of Nans': missingVal,
         'Percent of Nans':missingPer}

df_missing = pd.DataFrame(frame).sort_values(by='Percent of Nans',ascending=False)
print(df_missing)

# %%

# df.drop(['Unnamed: 0'], axis=1, inplace=True)
df['price'].fillna(df['price'].mean(), inplace = True)


# %%
