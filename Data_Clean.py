import pandas as pd 
def clean_data(df):
    df.drop_duplicates(inplace=True)
    df = df[df['price'] > 0]
    return df