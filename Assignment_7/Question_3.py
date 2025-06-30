import pandas as pd
df = pd.read_csv('sample_sales_data.csv')
print(df)
print(df.tail(15))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)