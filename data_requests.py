#!/bin/python3
import csv
import metoffer
import pandas as pd
import log_utils as log
import pprint

def request_data(lat=52.78263,long=-2.08490,fcast_type="day"):
  api_key = '60a57704-db3a-4e39-b216-4d5f8beec50d'
  M = metoffer.MetOffer(api_key)
  if fcast_type == "day":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.DAILY)
  if fcast_type == "th":
    fcast_obj = M.nearest_loc_forecast(lat, long, metoffer.THREE_HOURLY)

  data = metoffer.Weather(fcast_obj).data
  log.logger.info(pprint.pformat(data))

  return data

