#!/bin/python3
import metoffer
import datetime
import csv

deg_symbol = "°"
field_map = []
with open("map_item_names.csv","r") as file:
  csv_reader = csv.reader(file)
  item_name_map = dict(csv_reader)
file.close()

#Create a list for day and night data
# each day/night is a list within the list
# each list is structured as follows:
# day nr, item_name, value, units, pretty_item_name', 'pretty_val'' (val+vunit), day_name, day_of_month,month

def prepData(data):
  columns = ["day_nr","item_name","value","unit","pretty_item_name",pretty_val,day_name","dom","month"]

  #loop days (each item is dict)
  day_nr = 0
  for item in data:
    date_list = dateToList(item["timestamp"][0])
    for key in item.keys():
      item_name = key
      value = item[key][0]
      unit = item[key][1]
      day_name = date_list[0]
      dom = date_list[1]
      month = date_list[2]
      pretty_item_name = item_name_map[item_name]
      pretty_val = ""
      if "imestamp" in item_name:
        pretty_val = day_name + " " + dom + " " + month
      elif "emperature" in item_name:
        pretty_val = str(value) + deg_symbol + unit
      elif "irection" in item_name:
        pretty_val = str(value)
      else:
        pretty_val = str(value) + " " + unit
      row = [day_nr,item_name,value,unit,pretty_item_name,pretty_val,day_name,dom,month]
      print(row)

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
  api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
  M = metoffer.MetOffer(api_key)
  lat = 52.78263
  long = -2.08490
  daily_fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.DAILY)
  daily_data = metoffer.Weather(daily_fcast_obj).data

  prepData(daily_data)
#  temps = getDailyTemps(daytime_data)


main()
del day_data
del night_data

def dateToList(timestamp):
  out = []
  day_of_month = timestamp.strftime('-d') 
  dom_suffix = dayOfMonthSuffix(day_of_month)
  out.append(timestamp.strftime('%a'))
  out.append(timestamp.strftime('%-d' + dom_suffix))
  out.append(timestamp.strftime('%b'))
  return out

def requestData(lat=52.78263,long=-2.08490,type="DAILY"):
  api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
  M = metoffer.MetOffer(api_key)
  if type == "day":
    type = "DAILY"
  if type == "th":
    type = "THREE_HOURLY"

  fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.type)
  data = metoffer.Weather(fcast_obj).data

  return data

