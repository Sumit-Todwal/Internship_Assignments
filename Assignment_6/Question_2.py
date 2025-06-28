import pandas as pd
df1 = pd.DataFrame({'Name':['A1','A2','A3','A4'],
        'Age' :[20,21,22,23],
        'Marks':[87,97,93,85],
        'ID' :[1,2,3,4]
        })
df2 = pd.DataFrame({'Name':['A1','B2','B3','B4'],
        'Age' :[18,19,20,21],
        'Marks':[78,98,99,63],
        'ID':[1,2,3,5]
        })
res = df1.merge(df2, on="ID", how="inner")
# print(res)
result = df1.merge(df2, on="ID", how="left")
# print(result)
right = df1.merge(df2, on="ID", how="right")
# print(right)
# Index assigning....
df1.index = ['row1','row2','row3','row4']
df2.index = ['row1','row2','row3','row4']
#Index based join.
result = df1.join(df2,  how="inner", lsuffix="_df1", rsuffix="_df2")
# print(result)


#                    *** For handeling of missing values in resulting dataframe ***
#         -> in resulting dataframe if values does not match any part during left, right, inner and outer join then 
#                                   these values are assigned by NaN values.....

right_join = pd.merge(df1,df2, on="ID", how="right")
# print(right_join)

# df Join
Join = df1.join(df2, lsuffix="_df1",  rsuffix="_df2")
# print(Join)

# Comparing the Results....
# df.join():
#            -> in df.join(), Primarily used to join DataFrames based on their **index**
#                we can not join on the basis of keys. like on=""

# pd.merge():
#             -> in pd.merge(), Allows merging on **any column(s)**, even multiple keys
#                 Supports inner, left, right, outer joins with great control

# Merging with multiple keys.
Merging = pd.merge(df1,df2, on=["ID","Name"], how="inner")
print(Merging)