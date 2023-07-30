#!/bin/python3
import pandas as pd
import proj_utils as utils

deg_symbol = "°"

def main():
  lat = 52.78263
  long = -2.08490

  raw_daily_data = utils.request_data(lat,long,"day")
  raw_th_data = utils.request_data(lat,long,"th")
  daily_df = utils.prep_data(raw_daily_data)
  th_df = utils.prep_data(raw_th_data)

  th_df.to_csv('th_data.csv',index=False)
  daily_df.to_csv('daily_data.csv',index=False)

#  daily_df_filtered = daily_df[daily_df['pretty_item_name'].isin(['timestamp','Temp', 'Rain', 'Wind'])]

main()
