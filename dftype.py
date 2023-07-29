def show_value_types(dataframe):
  for column in dataframe.columns:
    for value in dataframe[column]:
      print(type(value))
