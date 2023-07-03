#!/bin/python3
import pandas as pd

data = {'col1': [1, 2, 3, 4, 5, 6, 7, 8],
        'col2': ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
        'col3': [10, 20, 30, 40, 50, 60, 70, 80],
        'col4': [True, False, True, False, True, False, True, False],
        'col5': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8],
        'col6': ['x', 'y', 'z', 'w', 'v', 'u', 't', 's'],
        'col7': [100, 200, 300, 400, 500, 600, 700, 800],
        'col8': [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8]}

df = pd.DataFrame(data)


for index, row in df.iterrows():
  print(f"Row Index: {index}")
  for column, value in row.iteritems():
    print(f"Column: {column}, Value: {value}")

