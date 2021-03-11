import pandas as pd
import numpy as np

def process_data(path_to_df):
    
    df1 = (
        pd.read_csv(path_to_df, header=None)
        .rename(columns = {0: 'Age', 1: "Workclass", 2: "Final Weight", 3: "Education", 4: "Education Num", 5: "Marital Status",  6: "Occupation", 7: "Relationship", 8: "Race", 9: "Sex", 10: "Capital Gain", 11: "Capital Loss", 12: "Hours per Week", 13: "Native Country", 14: "Salary"})
        .fillna(method="ffill")
    )
        
    return df1