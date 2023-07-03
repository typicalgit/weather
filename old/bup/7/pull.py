#!/bin/python3
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

  for i, item in enumerate(data):
    if i == 0:
      for i, key in enumerate(item.keys()):
        print(key)
        print(item[key])
  return data

def prep_data(data):
  i = 0
  formatted_data = []

  for dict in data:
    for key in dict.keys():
      dict[key] = dict[key][0] 
    value_only_data.append(dict)  

  for dict in value_only_data:
    if i < 1:
      df = pd.DataFrame(dict)
      i += 1
      continue
    # Append the dictionaries to the DataFrame
    df.update(pd.DataFrame(dict))

  return df


raw_data = requestDat()

final_data = prep_data(raw_data)
substring = 'irection'
filtered_df = final_data.filter(like=substring)

print(filtered_df)
