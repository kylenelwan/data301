import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def load_and_process(path):
    
    load = (
    pd.read_csv(path,header = None)
    .rename(columns={0:"Age",1:"Workclass",2:"Final Weight",3:"Education",4:"Education Num",5:"Marital Status",6:"Occupation",7:"Relationship",
                     8:"Race",9:"Sex",10:"Capital Gain",11:"Capital Loss",12:"Hours per Week",13:"Native Country",14:"Salary"})
    .dropna()
    .rename(index = lambda x: x + 1) 
    )
    
    return load
 
def load_and_process_two(url_or_path):
    
    df1 = (
        pd.read_csv(url_or_path)
        .rename(columns={0:"Age",1:"Workclass",2:"Final Weight",3:"Education",4:"Education Num",5:"Marital Status",6:"Occupation",7:"Relationship",
                     8:"Race",9:"Sex",10:"Capital Gain",11:"Capital Loss",12:"Hours per Week",13:"Native Country",14:"Salary"})
        .dropna()
        .rename(index = lambda x: x + 1)
    )
    
    return df1

def find_and_replace(dataframe, column_name, find, replace):
    dataframe[column_name] = dataframe[column_name].str.replace(find, replace, regex=True)
