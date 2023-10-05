import pandas as pd

def map_row_headings(data, mapping):
  # Create a pandas DataFrame from the data
  df = pd.DataFrame(data)
  
  # Map the row headings using the dictionary
  df.index = df.index.map(mapping.get)
  
  # Create a crosstab using the mapped row headings
  crosstab = pd.crosstab(index=df.index, columns=df.columns)
  
  return crosstab

def format_row_headings(crosstab, format_string):
    # Convert the row headings to datetime objects
    crosstab.index = pd.to_datetime(crosstab.index)

    # Format the row headings using the specified format string
    formatted_index = crosstab.index.strftime(format_string)

    # Update the crosstab with the formatted row headings
    crosstab.index = formatted_index

    return crosstab
```

You can use this function by passing your pandas crosstab and the desired format string as arguments. For example:

```python
import pandas as pd

# Create a sample crosstab
data = {'Timestamp': ['2022-01-01 12:00:00', '2022-01-02 12:00:00', '2022-01-03 12:00:00'],
        'Category': ['A', 'B', 'A']}
df = pd.DataFrame(data)

crosstab = pd.crosstab(df['Timestamp'], df['Category'])

# Call the format_row_headings function with the desired format string
formatted_crosstab = format_row_headings(crosstab, "%Y-%m-%d")

print(formatted_crosstab)
```
