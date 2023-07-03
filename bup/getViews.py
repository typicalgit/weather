#!/bin/python3
import pandas as pd
import projutils as utils

deg_symbol = "°"

def getDailyTemps(daily_data):
  date_list = []
  degreesC = ""
  day = ""
  data_out = []

  return data_out

def main():
  lat = 52.78263
  long = -2.08490

  raw_daily_data = utils.requestData(lat,long,"day")
  raw_th_data = utils.requestData(lat,long,"th")
  daily_dataframe = utils.prepData(raw_daily_data,"day")
  th_dataframe = utils.prepData(raw_th_data,"th")
  print(th_dataframe)
#  temps = getDailyTemps(data)

main()
