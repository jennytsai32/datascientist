# datasci
datasci is a python module aimed to simplify and shorten the data preprocessing process. You can clone the github repo to use this module. The folder includes the following files:<br>
(1) datasci.py: the module <br>
(2) test_jenny.py: test file including the example codes <br>
(3) flight_december.csv & flight_december copy.csv: sample datasets for testing file. The datasets are published by U.S. Department of Transportation and have been truncated for demo purposes.<br>
(4) README.md: a detailed description of the module <br><br>


The datasci module has functions/methods under two categories: (1) data preprocessing and (2) preliminary analysis. See below for the list of functions and documentations: <br>

*******DATA PREPROCESSING*******:<br>
(1) .size()<br>
    prints number of columns and rows in the dataframe in an easy-to-read format.<br><br>
    
(2) .missingReport(insight = False)<br>
    returns a report of variables with missing values and missing value percentage in relations to its sample size. If insight = True, prints recommendations for how to handle missing values.<br><br>
    
(3) .imputation(columns, impute, insight = False)<br>
    imputes the missing values with selected statistics.<br>
    :: columns: list of column names with missing values to be imputed.<br>
    :: impute: statistics to be imputed, including 'mean', 'median', 'mode', 'max', 'min', and 'other'. If 'other' is selected, users will be prompted to enter custom values to impute for each column.<br>
    :: insight: default = False. If True, prints a table comparing statistics before vs. after imputation.<br><br>
    
(4) .recode(column, oldVal, newVal, inplace=False)<br>
    recode the variable by replacing a list of old values with new values.<br>
    :: column: column name whose values to be recoded.<br>
    :: oldVal: list of original values within the variable/column.<br>
    :: newVal: list of new values to replace the old values.<br>
    :: inplace: default = False, which creates a new variable/column with new values. If True, new values replace the old values in the original variable/column.<br><br>
    
(5) .column_tolist(self)
    returns a clean list of all the columns
    :: self: the target data frame

*******PRELIMINARY ANALYSIS*******:<br>
(6) .eda(column, insight = False)<br>
    return a graph (histogram or bar chart) of the variable's distribution with descriptive statistics for exploratory data analysis.<br>
    :: column: column name, can be continuous variable or categorical variable.<br>
    :: insight: default = False. If True, prints recommendations for data imputation based on skewness of distribution of the variable.<br><br>

(7) .featureSelection(features, target)<br>
    returns a bar chart with top 10 important features predicting the target variable.<br>
    :: features: list of column names to be entered into the feature selection model (i.e., Random Forest).
    :: target: target variable name<br><br>

(8) .file_comparison(file_path1, file_path2)
    returns detail of differences between two files
    :: file_path1: first file to compare
    :: file_path2: second file to compare


*******recommendation packages*******:<br>
Package                      Version
---------------------------- ------------
absl-py                      2.0.0       
anyio                        4.0.0       
argon2-cffi                  23.1.0      
argon2-cffi-bindings         21.2.0      
arrow                        1.3.0       
asttokens                    2.4.0       
astunparse                   1.6.3       
async-lru                    2.0.4       
attrs                        23.1.0      
Babel                        2.13.0      
backcall                     0.2.0       
beautifulsoup4               4.12.2      
bleach                       6.0.0       
blinker                      1.7.0       
cachetools                   5.3.1       
certifi                      2023.7.22   
cffi                         1.16.0      
charset-normalizer           3.3.0       
click                        8.1.7       
clock                        0.1
colorama                     0.4.6
comm                         0.1.4
contourpy                    1.1.1
cupy-cuda12x                 12.2.0
cycler                       0.12.0
debugpy                      1.8.0
decorator                    5.1.1
defusedxml                   0.7.1
exceptiongroup               1.1.3
executing                    2.0.0
fastjsonschema               2.18.1
fastrlock                    0.8.2
filelock                     3.12.4
Flask                        3.0.0
flatbuffers                  23.5.26
fonttools                    4.43.0
fqdn                         1.5.1
fsspec                       2023.9.2
gast                         0.5.4
google-auth                  2.23.2
google-auth-oauthlib         1.0.0
google-pasta                 0.2.0
grpcio                       1.59.0
h5py                         3.9.0
idna                         3.4
ipykernel                    6.25.2
ipython                      8.16.0
isoduration                  20.11.0
itsdangerous                 2.1.2
jedi                         0.19.0
Jinja2                       3.1.2
joblib                       1.3.2
json5                        0.9.14
jsonpointer                  2.4
jsonschema                   4.19.1
jsonschema-specifications    2023.7.1
jupyter_client               8.3.1
jupyter_core                 5.3.2
jupyter-events               0.7.0
jupyter-lsp                  2.2.0
jupyter_server               2.7.3
jupyter_server_terminals     0.4.4
jupyterlab                   4.0.6
jupyterlab-pygments          0.2.2
jupyterlab_server            2.25.0
kaleido                      0.2.1
keras                        2.14.0
kiwisolver                   1.4.5
libclang                     16.0.6
lightgbm                     4.1.0
Markdown                     3.4.4
MarkupSafe                   2.1.3
matplotlib                   3.8.0
matplotlib-inline            0.1.6
mistune                      3.0.2
ml-dtypes                    0.2.0
mpmath                       1.3.0
nbclient                     0.8.0
nbconvert                    7.9.2
nbformat                     5.9.2
nest-asyncio                 1.5.8
networkx                     3.1
notebook                     7.0.4
notebook_shim                0.2.3
np                           1.0.2
numpy                        1.24.3
nvidia-cuda-runtime-cu12     12.2.140
nvidia-pyindex               1.0.9
oauthlib                     3.2.2
opt-einsum                   3.3.0
overrides                    7.4.0
packaging                    23.2
pandas                       2.1.1
pandocfilters                1.5.0
parso                        0.8.3
patsy                        0.5.3
pickleshare                  0.7.5
Pillow                       10.0.1
pip                          23.2.1
platformdirs                 3.10.0
plotly                       5.17.0
prometheus-client            0.17.1
prompt-toolkit               3.0.39
protobuf                     4.24.4
psutil                       5.9.5
pure-eval                    0.2.2
pyasn1                       0.5.0
pyasn1-modules               0.3.0
pycparser                    2.21
Pygments                     2.16.1
pyparsing                    3.1.1
python-dateutil              2.8.2
python-json-logger           2.0.7
pytz                         2023.3.post1
pywin32                      306
pywinpty                     2.0.11
PyYAML                       6.0.1
pyzmq                        25.1.1
referencing                  0.30.2
requests                     2.31.0
requests-oauthlib            1.3.1
retrying                     1.3.4
rfc3339-validator            0.1.4
rfc3986-validator            0.1.1
rpds-py                      0.10.3
rsa                          4.9
scikit-learn                 1.3.1
scipy                        1.11.3
seaborn                      0.13.0
Send2Trash                   1.8.2
setuptools                   68.2.2
six                          1.16.0
sniffio                      1.3.0
soupsieve                    2.5
stack-data                   0.6.3
statsmodels                  0.14.0
sympy                        1.12
tenacity                     8.2.3
tensorboard                  2.14.1
tensorboard-data-server      0.7.1
tensorflow                   2.14.0
tensorflow-estimator         2.13.0
tensorflow-intel             2.14.0
tensorflow-io-gcs-filesystem 0.31.0
termcolor                    2.3.0
terminado                    0.17.1
threadpoolctl                3.2.0
tinycss2                     1.2.1
tomli                        2.0.1
torch                        2.1.0+cu121
torchaudio                   2.1.0+cu121
torchvision                  0.16.0+cu121
tornado                      6.3.3
traitlets                    5.10.1
types-python-dateutil        2.8.19.14
typing_extensions            4.5.0
tzdata                       2023.3
tzlocal                      5.2
uri-template                 1.3.0
urllib3                      2.0.6
utils                        1.0.1
wcwidth                      0.2.8
webcolors                    1.13
webencodings                 0.5.1
websocket-client             1.6.3
Werkzeug                     3.0.0
wheel                        0.41.2
wrapt                        1.14.1
xgboost                      2.0.0
<br>