#!/bin/python3
import metoffer

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

