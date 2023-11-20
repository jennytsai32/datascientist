# CS Foundations Final Project
# Team #8
# Jenny Tsai & Jiazu Zhang


# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class datasci():
    def __init__(self, df):
        self.df = df
        self.shape = df.shape
        self.nrows = df.shape[0]
        self.ncols = df.shape[1]

    def size(self):
        return f"There are {self.nrows} rows and {self.ncols} columns in the dataset."
        
    def missingReport(self):
        missingVal = self.df[self.df.columns[self.df.isnull().any()].tolist()].isnull().sum()
        missingPer = round((missingVal * 100/ self.nrows), 2)

        frame = {'Num of Nans': missingVal,
                'Percent of Nans': missingPer}

        missing_report = pd.DataFrame(frame).sort_values(by='Percent of Nans', ascending = False)

        print(f'The following variables contains over 80% missing values:')
        print(missing_report[missing_report['Percent of Nans']>=80].index.tolist())
        print('')

        return missing_report
    

    def imputation(self, columns, impute = 'mean', check = False):
        if impute == 'mean':
            for col in columns:
                self.df[col].fillna(self.df[col].mean(), inplace = True)

        elif impute == 'median':
            for col in columns:
                self.df[col].fillna(self.df[col].median(), inplace = True)
        
        elif impute == 'max':
            for col in columns:
                self.df[col].fillna(self.df[col].max(), inplace = True)

        elif impute == 'min':
            for col in columns:
                self.df[col].fillna(self.df[col].min(), inplace = True)
    
        elif impute == 'other':

            for col in columns:
                print(f'Please enter the value to impute "{col}":')
                x = input()
                self.df[col].fillna(x, inplace = True)
        
        if check == True:
            print('Number of missing values after imputation:')
            print(self.df[columns].isnull().sum())

    def recode(self, column, oldVal, newVal, inplace=False):
        new_name = str(column) + '_NEW'
        self.df[new_name] = self.df[column].replace(oldVal, newVal)

        if inplace == True:
            self.df[column].replace(oldVal, newVal, inplace=True)
            return self.df[column].value_counts()
        
        else:
            return self.df[new_name].value_counts()



            
            




