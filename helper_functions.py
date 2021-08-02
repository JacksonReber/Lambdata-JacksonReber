def null_count(df):
    df.isnull.sum()
    return df 

def train_test_split(df, frac):
    train_test_split(df, frac=0.2)
    return df, frac