#!/bin/python3
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
  for item in data:
    for key in item.keys():
      print(key)

  return data

requestDat()

