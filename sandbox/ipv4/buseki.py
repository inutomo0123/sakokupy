import pandas as pd

df = pd.read_csv('../record.txt', delimiter='|', header=None,
                 names=('registry', 'cc', 'type', 'start',
                        'value', 'date', 'status', "わからん"))

#print(df)

print(df[df.type == 'ipv4'][['start', 'value']])
