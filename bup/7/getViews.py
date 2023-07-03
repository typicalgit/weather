#!/bin/python3
import pandas as pd
import projutils as utils

deg_symbol = "°"

def main():
  lat = 52.78263
  long = -2.08490

  raw_daily_data = utils.requestData(lat,long,"day")
  raw_th_data = utils.requestData(lat,long,"th")
  daily_df = utils.prepData(raw_daily_data,"day")
  th_df = utils.prepData(raw_th_data,"th")

  ct = pd.crosstab(daily_df['timestamp'], daily_df['pretty_val'])
  print(ct)

#  # iterate through row headings, column headings, and values
#  for row in ct.index:
#      for col in ct.columns:
#          value = ct.loc[row, col]
#          print(f'Row: {row}, Column: {col}, Value: {value}')
               


  th_df.to_csv('th_data.csv',index=False)
  daily_df.to_csv('daily_data.csv',index=False)
  daily_df_filtered = daily_df[daily_df['pretty_item_name'].isin(['timestamp','Temp', 'Rain', 'Wind'])]

main()
