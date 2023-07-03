#!/bin/python3
import csv
import metoffer
import pandas as pd

deg_symbol = "°"

def readCSV(file_path,out_type):
  with open(file_path) as file:
    csv_reader = csv.reader(file)
    if out_type == "dict":
      csv_out = dict(csv_reader)
    if out_type == "list":
      csv_out = list(csv_reader)
  file.close()
  return csv_out

#Create a list for day and night data
# each day/night is a list within the list
# each list is structured as follows:
# day nr, item_name, value, units, pretty_item_name', 'pretty_val'' (val+vunit), day_name, day_of_month,month

def prepData(data,data_type):
  if data_type == "day":
    item_name_map = readCSV("map_daily_item_names.csv","dict")
  if data_type == "th":
    item_name_map = readCSV("map_th_item_names.csv","dict")

  data_out = []
  columns = ["day_nr","item_name","value","unit","pretty_item_name","pretty_val","day_name","dom","month"]

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
      data_out.append( row )
  panda_out = pd.DataFrame(data_out,columns=columns)
  return panda_out


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

def requestData(lat=52.78263,long=-2.08490,fcast_type="day"):
  api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
  M = metoffer.MetOffer(api_key)
  if fcast_type == "day":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.DAILY)
  if fcast_type == "th":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.THREE_HOURLY)

  data = metoffer.Weather(fcast_obj).data

  return data


