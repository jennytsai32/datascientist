# %% import libraries and read the dataset

from datasci import datasci
import pandas as pd


df = pd.read_csv("flights_december.csv")
m = datasci(df)

print(df.head())


#%% dataset size
print(m.size())


#%% (1) missing value report
print(m.missingReport(insight=True))


# %% (2a) EDA - continuous variable
m.eda('TAXI_IN', insight=True)


# %% (2b) EDA - categorical variable
print(m.eda('AIRLINE'))


# %% (3) missing value imputation
m.imputation(columns=['TAXI_IN','ARRIVAL_TIME'], impute='median', insight=True)

# %% (4) variable recoding
print(df['AIRLINE'].value_counts())


#%%
old = ['AA','DL']
new = ['American Airline','Delta']

m.recode(column = 'AIRLINE', oldVal=old, newVal=new, inplace=True)

# %% data-cleaning using pandas

df.drop(['YEAR',                   # year = 2015, add no value to the model
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
        'CANCELLED',               # variable irrelevant to our analysis
        'AIRLINE'],              
        axis=1, inplace=True)

df.dropna(subset=['ARRIVAL_DELAY'], inplace=True)

df['ARRIVAL_DELAY'] = df['ARRIVAL_DELAY'].apply(lambda x:'1' if x>0 else '0')


# %% (5) feature selection
features = df.iloc[:, 0:-1].columns
target = 'ARRIVAL_DELAY'
m.featureSelection(features, target)


#%% (6) File comparison
datasci.file_comparsion("flights_december.csv", "flights_december copy.csv")

#%% (7) Column to list

m.column_tolist()
# %%
