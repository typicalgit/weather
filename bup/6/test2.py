#!/bin/python3
import pandas as pd

# create dataframe
data = {'fruit': ['apple', 'banana', 'orange', 'apple', 'banana', 'orange'],
        'color': ['red', 'yellow', 'orange', 'green', 'yellow', 'orange']}
df = pd.DataFrame(data)

# create crosstab
ct = pd.crosstab(df['fruit'], df['color'])

# iterate through row headings, column headings, and values
for row in ct.index:
    for col in ct.columns:
        value = ct.loc[row, col]
        print(f'Row: {row}, Column: {col}, Value: {value}')
