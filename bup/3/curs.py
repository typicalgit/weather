#!/bin/python3
import curses


def draw_days(stdscr,data,key):
  if k == curses.KEY_RIGHT:
     

#  GET HEIGHT AND WIDTH
  height, width = stdscr.getmaxyx()

# DEFINE PAD FOR DATA
  pad = curses.newpad(height-2,width-2)

  pad.addstr(0,0,"TeStT")
  stdscr.refresh()
  pad.refresh(0,0,0,0,height-2,width-2)
### END


def draw_menu(stdscr,key):
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

def draw_week():
  return True

def main_keymon(stdscr):
  k = stdscr.getch()

def main(stdscr):
  mode = 'm'
  key = 0

  while  key != ord('q'):
    stdscr.clear()
    if mode == 'm':
      draw_menu(stdscr,key)
    elif mode == 'd':
      draw_days(stdscr,'',key)
    elif mode == 'w':
      draw_week()
    stdscr.refresh()
    key = stdscr.getch()
    if key == ord('d'):
      mode = 'd'

if __name__ == "__main__":
  curses.wrapper(main)
