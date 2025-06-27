import pandas as pd
# Creating a pandas series from dictionary.
data = {
    "Name" : "Vikas",
    "Age" : 20,
    "State" : "Rajasthan"
}
ps = pd.Series(data)
print(ps)

# Part 2
# Creating a pandas series from List.

my_List = [10,0,30,40]
pseries = pd.Series(my_List)
print(pseries)

# Part3
# Accessing the elements of series in pandas.
Element = ps["Name"]
print(Element)