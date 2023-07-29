#!/bin/python3
import csv
import metoffer
import pandas as pd

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

def requestData(lat=52.78263,long=-2.08490,fcast_type="day"):
  api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
  M = metoffer.MetOffer(api_key)
  if fcast_type == "day":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.DAILY)
  if fcast_type == "th":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.THREE_HOURLY)

  data = metoffer.Weather(fcast_obj).data

  return data


