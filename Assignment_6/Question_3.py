import pandas as pd
df1 = pd.DataFrame({
    "Name" : ['Sumit','Ajay','Shubham','Abhishek'],
    "Age" : [21,19,24,22],
    "Section" : ['A','B','C','D'],
    "ID" : [1,2,3,4]
})
df2 = pd.DataFrame({
    "Name" : ['Rajat','shreyans','chirag','akshat'],
    "Age" : [20,21,21,19],
    "Section" : ['A','B','C','D'],
    "ID" : [1,2,3,4]
})
df3 = pd.DataFrame({
    "Country" : ['India','US','UK','Canada'],
    "State" : ['Raj','UP','UK','Jammu'],
    "Rank" : [1,2,3,4],
    "ID" : [1,2,3,4]
})

New_Dataframe =  pd.concat([df1,df2])
print(New_Dataframe)

Merge = New_Dataframe.merge(df3, on="ID")
print(Merge)

# df.join():
#            -> in df.join(), Primarily used to join DataFrames based on their **index**
#                we can not join on the basis of keys. like on=""

# pd.merge():
#             -> in pd.merge(), Allows merging on **any column(s)**, even multiple keys
#                 Supports inner, left, right, outer joins with great control