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

        print(f'The following variables contains over 80% missing values and are recommended to be removed:')
        print(missing_report[missing_report['Percent of Nans']>=80].index.tolist())
        print('')

        return missing_report


# %%
