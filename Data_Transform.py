# from datetime import datetime

def add_features(df):
    # current_year = datetime.now().year
    # df['car_age'] = current_year - df['year']
    # df = df.drop('year', axis=1)
    # return df 
    df['year'].astype('int')
    return df
