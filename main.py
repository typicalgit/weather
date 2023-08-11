#!/bin/python3
import pandas as pd
import data_prep as dp
import signal_handler as sh
import curses_gui as gui

def main():
  sh.setup_signal_handlers()

  lat = 52.78263
  long = -2.08490

  dp.get_data(lat,long)
  gui.start_curses()



main()
