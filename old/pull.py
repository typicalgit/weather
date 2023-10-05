#!/bin/python3
import log_utils as log
import datetime
import pandas as pd
import pprint
import metoffer

def requestDat(lat=52.78263,long=-2.08490,fcast_type="th"):
  api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
  M = metoffer.MetOffer(api_key)
  if fcast_type == "day":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.DAILY)
  if fcast_type == "th":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.THREE_HOURLY)

  data = metoffer.Weather(fcast_obj).data
  log.logger.info(pprint.pformat(data))

  return data

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


raw_data = requestDat(fcast_type='day')
final_data = prep_data(raw_data)

#substring = 'irection'
#filtered_df = final_data.filter(like=substring)
