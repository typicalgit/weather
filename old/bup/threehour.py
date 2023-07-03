#!/bin/python3
import pandas as pd
import projutils as utils

deg_symbol = "°"
day_data = []
night_data = []

def getDaysOrNights(forecast_data, d_or_n="d"):
  out = []
  for i in range(0,10):
    if i % 2 == 0 and d_or_n == "d":
      out.append(forecast_data[i])
    elif i % 2 != 0 and d_or_n == "n":
      out.append(forecast_data[i])
      
  return out

def getDailyTemps(daily_data):
  out = []
  date_list = []
  degreesC = ""
  day = ""
  for day in daily_data:
    temp_str = day["Day Maximum Temperature"] 
    time_temp = []
    degreesC = temp_str[0]
    date_list = dateToList( day["timestamp"][0] )
    day = date_list[0]
    time_temp.append(day)
    time_temp.append(degreesC)
    out.append(time_temp)
  return out

def main():
  lat = 52.78263
  long = -2.08490

  raw_data = utils.requestDat(lat,long,"day")
  data = utils.prepData(raw_data)
#  temps = getDailyTemps(data)

main()
