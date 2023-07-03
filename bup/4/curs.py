#!/bin/python3
import sys
import signal
import curses

def signal_handler(sig, frame):
  print('Exiting gracefully...')
  sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def quitter():
  sys.exit(0)

def draw_days(stdscr,data):
  if key == curses.KEY_RIGHT:
    print('placeholder')

  height, width = stdscr.getmaxyx()

# DEFINE PAD FOR DATA
  pad = curses.newpad(height-2,width-2)

  pad.addstr(0,0,"TeStT")
  stdscr.refresh()
  pad.refresh(0,0,0,0,height-2,width-2)
### END


def draw_menu(stdscr):
  # Initialization
  height, width = stdscr.getmaxyx()

  # Declaration of strings
  title = "Weather Forecast"[:width-1]
  statusbarstr = "Press 'q' to exit | press 'd' for days | press 'w' for weeks"

  # Centering calculations
  start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
  start_y = int((height // 2) - 2)

  # Render status bar
  stdscr.addstr(height-1, 0, statusbarstr)
  stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))

  # BOLD TITLE
  stdscr.attron(curses.A_BOLD)
  stdscr.addstr(start_y, start_x_title, title)
  stdscr.attroff(curses.A_BOLD)

def draw_week(stdscr):
  return True

def main_keymon(stdscr):
  k = stdscr.getch()

def main(stdscr):
  stdscr.clear()
  draw_menu(stdscr)

if __name__ == "__main__":
  curses.wrapper(main)
import sys
import signal


