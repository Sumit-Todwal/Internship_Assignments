import pandas as pd
# python dataframe with two dimensional python list
data = [
    ['A','B','C','D'],[1,2,3,4]
]
df = pd.DataFrame(data)
print(df)
# Create dataframe from python dict.
dictionary = {
    "Name": ['Aryan'],
    "Section": ['D'],
    "Age" : [20],
    "School" : ["Emmanuel"]
}
dframe = pd.DataFrame(dictionary)
print(dframe)
# Create pandas dataframe using list of lists.
New_data = [[1,2,3],['A','B','C'],["Hello","India","World"]]
datafr = pd.DataFrame(New_data,columns=["ID","Letter","Country"])
print(datafr)
# Create a pandas dataframe using list of tuples.
datatuple = [("Hi","Hello","Hey"),(1,2,3),("News","first","last")]
df = pd.DataFrame(datatuple)
print(df)
# Create a pandas dataframe using list of dictionary.
datadictionary = [
    {"Name":"Sumit","Age":21},{"Year":2025,"Month":"June"},{"Song":"Music"}
]
df = pd.DataFrame(datadictionary)
print(df)