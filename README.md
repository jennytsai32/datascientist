# datasci
datasci is a python module aimed to simplify and shorten the data preprocessing process. You can clone the github repo to use this module. The folder includes the following files:<br>
(1) datasci.py: the module
(2) test_jenny.py: test file including the example codes
(3) flight_december.csv & flight_december copy.csv: datasets for testing file
(4) README.md:detailed description of the module <br><br>


The datasci module has functions/methods under two categories: (1) data preprocessing and (2) preliminary analysis. See below for the list of functions and documentations:

*******DATA PREPROCESSING*******:<br>
(1) .size()
    prints number of columns and rows in the dataframe in an easy-to-read format.
    
(2) .missingReport(insight = False)
    returns a report of variables with missing values and missing value percentage in relations to its sample size. If insight = True, prints recommendations for how to handle missing values.
    
(3) .imputation(columns, impute, insight = False)
    imputes the missing values with selected statistics.
    :: columns: list of column names with missing values to be imputed.
    :: impute: statistics to be imputed, including 'mean', 'median', 'mode', 'max', 'min', and 'other'. If 'other' is selected, users will be prompted to enter custom values to impute for each column.
    :: insight: default = False. If True, prints a table comparing statistics before vs. after imputation.
    
(4) .recode(column, oldVal, newVal, inplace=False)
    recode the variable by replacing a list of old values with new values.
    :: column: column name whose values to be recoded.
    :: oldVal: list of original values within the variable/column.
    :: newVal: list of new values to replace the old values.
    :: inplace: default = False, which creates a new variable/column with new values. If True, new values replace the old values in the original variable/column.
    
(5) .column_tolist()


*******PRELIMINARY ANALYSIS*******:<br>
(6) .eda(column, insight = False)
    return a graph (histogram or bar chart) of the variable's distribution with descriptive statistics for exploratory data analysis.
    :: column: column name, can be continuous variable or categorical variable.
    :: insight: default = False. If True, prints recommendations for data imputation based on skewness of distribution of the variable.

(7) .featureSelection(features, target)
    returns a bar chart with top 10 important features predicting the target variable.
    :: features: list of column names to be entered into the feature selection model (i.e., Random Forest).
    :: target: target variable name

(8) .file_comparison(file_path1, file_path2)



