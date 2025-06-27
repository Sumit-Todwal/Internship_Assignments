import pandas as pd

df = pd.DataFrame({'Name': ['Sumit', 'Aryan'], 'Age': [21, 22]})

# Method 1: Using iterrows()
for index, row in df.iterrows():
    print(index, row['Name'], row['Age'])

# Method 2: Using itertuples()
for row in df.itertuples():
    print(row.Index, row.Name, row.Age)

# Can also be done by using Slicing but it will only give some portion.
#like..
print(df.loc[0:1])
print(df.loc[1:2])


# Selecting rows in pandas dataframe based on conditions.

print(df[df['Age']>21])

# Select any row from a dataframe using iloc.

print(df.iloc[0])

# Limited row selection with given column.
print(df.loc[0:1,"Name"])

# Drop rows from the dataframe based on certain condition apply on a column.
new_df = df.drop(df[df['Age']>21].index)
print(new_df)

# Insert Row at given position in pandas dataframe.
df.insert(1,"Section",["D","E"])
print(df)

# Create a List from rows in pandas dataframe.
List = df.values.tolist()
print(List)