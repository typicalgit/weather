#!/bin/python3
import csv
import metoffer
import pandas as pd
import log_utils as log
import datetime
import pprint
import data_requests as req
import io_utils as io


deg_symbol = "°"


def read_csv(file_path,out_type):
  with open(file_path) as file:
    reader = csv.reader(file)
    if out_type == "dict":
      result = {}
      for row in reader:
        key = row[0]
        values = row[1:]
        result[key] = values
      csv_out = dict(csv_reader)
    if out_type == "list":
      result = []
      result = list(reader)
  file.close()
  return result


def dateToList(timestamp):
  date_list = []
  day_of_month = timestamp.strftime('%-d')
  dom_suffix = dayOfMonthSuffix(day_of_month)
  date_list.append(timestamp.strftime('%a'))
  date_list.append(timestamp.strftime('%-d' + dom_suffix))
  date_list.append(timestamp.strftime('%b'))
  return date_list

def dayOfMonthSuffix(dom):
  suffix = ""

  if dom[-1:] == '3' and dom != '13':
    suffix = "rd"
  elif dom[-1:] == '2' and dom != '12':
    suffix = "nd"
  elif dom[-1:] == '1' and dom != '11':
    suffix = "st"
  else:
    suffix = "th"
  return suffix


### DATAFRAMES
def show_value_types(dataframe):
  for column in dataframe.columns:
    print(column)
    for i,value in enumerate(dataframe[column]):
      if i > 0:
        continue
      print(type(value))
      print(value)

def replace_tuples(df):
  for column in df.columns:
    if df[column].dtype == 'object':
      if column == 'timestamp':
        df['daynight'] = df[column].apply(lambda x: x[1] if isinstance(x, tuple) and len(x) > 1 else None)
        df['datetime'] = df[column].apply(lambda x: x[0] if isinstance(x, tuple) else None)
      df[column] = df[column].apply(lambda x: x[0] if isinstance(x, tuple) else x)

  df.set_index('timestamp', inplace=True)
  return df 


def prep_data(data):
  df = pd.DataFrame(data)
  value_df = replace_tuples(df)
  show_value_types(value_df)
# USEFUL FOR CREATING MAP OF COL HEAD TO UNITS
#  unit_df = df.applymap(lambda x: x[1] if isinstance(x, tuple) else x)

#  df = df.applymap(lambda x: ';'.join(map(str, x)))


  ##filtered_df = value_df.filter(like='imestamp')
  ##print(filtered_df)
  return value_df

raw_data = req.request_data(fcast_type='day')
final_data = prep_data(raw_data)

#substring = 'irection'
#filtered_df = final_data.filter(like=substring)


def get_data(lat,long):

  raw_daily_data = req.request_data(lat,long,"day")
  raw_th_data = req.request_data(lat,long,"th")

  th_df = prep_data(raw_th_data)
  daily_df = prep_data(raw_daily_data)
  day_df = daily_df[daily_df['daynight'] == 'Day']
  night_df = daily_df[daily_df['daynight'] == 'Night']

## WRITE DATA AS READABLE FORMAT
## NOTE THS IS NOT USED BY THE PROJECT, ONLY FOR TESTING
  day_df.to_csv('data/day_data.csv',index=False)
  night_df.to_csv('data/night_data.csv',index=False)
  th_df.to_csv('data/th_data.csv',index=False)

## WRITE OUT DATA AS PICKLE FILES
  io.write_pickle(day_df,'day_data')
  io.write_pickle(night_df,'night_data')
  io.write_pickle(th_df,'th_data')
