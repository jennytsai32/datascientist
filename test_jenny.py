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

df.drop(['YEAR',                    # year = 2015, add no value to the model
             'FLIGHT_NUMBER',           # too many categories and will cause trouble in one-hot encoding
             'TAIL_NUMBER',             # too many categories and will cause trouble in one-hot encoding
             'ARRIVAL_TIME',            # post-departure info
             'CANCELLATION_REASON',     # post-departure info + cancelled flights never depart
             'AIR_SYSTEM_DELAY',        # post-departure info
             'SECURITY_DELAY',          # post-departure info
             'AIRLINE_DELAY',           # post-departure info
             'WEATHER_DELAY',           # post-departure info
             'LATE_AIRCRAFT_DELAY',     # post-departure info
             'ORIGIN_AIRPORT',          # too many categories and will cause trouble in one-hot encoding
             'DESTINATION_AIRPORT',     # too many categories and will cause trouble in one-hot encoding
             'ELAPSED_TIME',            # post-departure info
             'AIR_TIME',                # post-departure info
             'WHEELS_ON',               # post-departure info
             'TAXI_IN',                 # post-departure info
             'DIVERTED',                # variable irrelevant to our analysis
             'CANCELLED',
             'AIRLINE'],              # variable irrelevant to our analysis

            axis=1, inplace=True)

# %%
# Drop rows where target value is missing (the missing records are either cancelled flights or diverted flights)
df.dropna(subset=['ARRIVAL_DELAY'], inplace=True)


# %%
# Convert into binary target for classification (1 = delay, 0 = not delay)
df['ARRIVAL_DELAY'] = df['ARRIVAL_DELAY'].apply(lambda x:'1' if x>0 else '0')

# %%
Y = df.values[:, -1]
X = df.values[:, 0:-1]
names = df.iloc[:, 0:-1].columns

m.feature_selection(X=X, Y=Y, feature_names=names)




# %%
