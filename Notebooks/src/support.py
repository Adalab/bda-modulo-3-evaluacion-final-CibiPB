
import pandas as pd
import numpy as np



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
    