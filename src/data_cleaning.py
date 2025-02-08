def clean_data(df):
    """清理數據"""
    df = df.drop_duplicates()
    df = df.dropna()
    return df
