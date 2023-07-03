#!/bin/python3
import metoffer
import datetime
import pprint

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

def dateToList(timestamp):
  out = []
  day_of_month = timestamp.strftime('-d') 
  dom_suffix = dayOfMonthSuffix(day_of_month)
  out.append(timestamp.strftime('%a'))
  out.append(timestamp.strftime('%-d' + dom_suffix))
  out.append(timestamp.strftime('%b'))
  return out

def getDays(forecast_data):
  out = []
  for i in range(0,10):
    if i % 2 == 0:
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


api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
M = metoffer.MetOffer(api_key)
lat = 52.78263
long = -2.08490
f_three_hour = M.nearest_loc_forecast(lat, long, metoffer.THREE_HOURLY)
f_daily = M.nearest_loc_forecast(lat, long, metoffer.DAILY)

three_hour = metoffer.Weather(f_three_hour).data
daily = metoffer.Weather(f_daily).data

day_data = getDays(daily)
temps = getDailyTemps(day_data)

pprint.pprint(day_data)


