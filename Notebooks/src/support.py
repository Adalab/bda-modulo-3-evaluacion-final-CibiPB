
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import KNNImputer



def remove_duplicate_rows(df):
        
    """Remove rows that have values duplicated in all columns"""
    
    rows_before = len(df)
    df = df.drop_duplicates(keep='first')  # Removes duplicates, keeping the first occurrence
    rows_after = len(df)
    dropped_rows_count = rows_before - rows_after
    
    print(f'There were {rows_before} rows, and {dropped_rows_count} duplicated rows were deleted.\nNew row count: {rows_after} rows')
    
    return df



def float_to_integer(df, list_cols_update):
        
    """Convert specified float columns to integers"""
        
    for col in list_cols_update:   
        try:    
            df[col] = pd.to_numeric(df[col], errors='coerce').astype('Int64') #Int64 to maintaing the nulls
        except: df[col] = np.nan
        
    return df
    
    
    
def num_and_cate(df, num_col, cate_col):
    sns.boxplot(x=cate_col, y=num_col, data=df)
    plt.title(f'Correlation of {cate_col} and {num_col}')
    

def num_and_num (df, col1, col2):
    
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    sns.scatterplot(x=df[col1], y=df[col2], ax=axes[0])
    sns.regplot(x=df[col1], y=df[col2], ax=axes[1])
    plt.show()