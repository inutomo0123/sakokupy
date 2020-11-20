import pandas as pd

df = pd.read_csv('record.txt', delimiter='|', header=None,
                 names=('registry', 'cc', 'type', 'start',
                        'value', 'date', 'status', "わからん"))

print(type(df))

print(df)

print(df.groupby('registry').groups.keys())

print(df.groupby('cc').groups.keys())

print(df.groupby('type').groups.keys())

print(df['start'].head())

print(df['value'].tail(100))

print(df['date'].head())


print(df.groupby('status').groups.keys())
# ['allocated', 'assigned', 'available', 'reserved']
