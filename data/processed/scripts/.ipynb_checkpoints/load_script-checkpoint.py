import pandas as pd

def process_data(path_to_df):
    
    df1 = (
        pd.read_csv(path_to_df, header=None)
        .rename(columns = {0: 'Age', 1: "Workclass", 2: "Final Weight", 3: "Education", 4: "Education Num", 5: "Marital Status",  6: "Occupation", 7: "Relationship", 8: "Race", 9: "Sex", 10: "Capital Gain", 11: "Capital Loss", 12: "Hours per Week", 13: "Native Country", 14: "Salary"})
        .fillna(method="ffill")
        .drop(columns={'Education Num', 'Final Weight', 'Capital Gain', 'Capital Loss'})
    )
        
    return df1

def find_and_replace(dataframe, column_name, find, replace):
    dataframe[column_name] = dataframe[column_name].str.replace(find, replace, regex=True)