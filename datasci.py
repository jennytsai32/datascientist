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

        print(f'The following variables contains over 70% missing values:')
        print(missing_report[missing_report['Percent of Nans']>=70].index.tolist())
        print('')

        return missing_report
    

    def imputation(self, columns, impute = 'mean', check = False):
        if impute == 'mean':
            for col in columns:
                self.df[col].fillna(self.df[col].mean(), inplace = True)

        elif impute == 'median':
            for col in columns:
                self.df[col].fillna(self.df[col].median(), inplace = True)
        
        elif impute == 'mode':
            for col in columns:
                self.df[col].fillna(self.df[col].mode(), inplace = True)
        
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
        
    def eda(self, column):
        if isinstance(self.df[column][0], (np.int64, np.int32, np.float32, np.float64)):
    
            data = {'N':[len(self.df[column])],
                    '# of Nans':[self.df[column].isnull().sum()],
                    'Mean':[self.df[column].mean()],
                    'Std':[self.df[column].std()],
                    'Median':[self.df[column].median()],
                    'Max':[self.df[column].max()],
                    'Min':[self.df[column].min()]
                    }
            descr = pd.DataFrame.from_dict(data, orient='index', columns=[column]).round(2)

            plt.hist(self.df[column], color = "#108A99")
            plt.axvline(self.df[column].mean(), color='r', label='mean')
            plt.axvline(self.df[column].median(), color='blue', linestyle='dashed',label='median')
            plt.legend()
            plt.xlabel(column)

            plt.show()
            
            return descr
        
        else:

            self.df[column].value_counts(sort=False).plot.bar(rot=0)
            plt.show()
            return self.df[column].value_counts()

    def column_tolist (self):
        x = self.columns
        temp = []
        for i in x:
            temp.append(i)
        return temp
        

    def file_comparsion(file1_path , file2_path):
        try: 
            with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
                print('Comparison Started...')
                Indicator = True
                for line_num, (line1, line2) in enumerate(zip(f1, f2), start = 1):
                    if line1 != line2:
                        print(f'\n Difference found at line {line_num}: \n Orignial File: {line1} \n Target File: {line2}')
                        column1 = line1.split()
                        column2 = line2.split()
                        for col_num, (col1, col2) in enumerate(zip(f1, f2), start = 1):
                            if col1 != col2:
                                print(f"\n Difference found at column {col_num}: \n Orignial File: {col1} \n Target File: {col2}")
                        Indicator = False
            if Indicator == True:
                print('\n Original and target files have same structure and content.')
            
            return 'Comparison Completed'
        except Exception as e:
            print(f'Error:{e}')
            return False            





# %%
