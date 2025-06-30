import pandas as pd

df = pd.DataFrame({'date': ['2024-12-20', '2025-01-15', '2025-06-28']})
df['date'] = pd.to_datetime(df['date'])

# Extract parts of the date
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['day_name'] = df['date'].dt.day_name()

filtered = df[df['date'] > '2025-01-01']
print(filtered)
print(df['year'])
print(df['month'])
print(df['date'])
print(df['day_name'])