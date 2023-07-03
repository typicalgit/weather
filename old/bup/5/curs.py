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

def draw_list(win,list,start_x,start_y,gap_x=0,gap_y=0,add_max_item_len_to_gap_y=False):
  pos = 0
  x = startx
  y = start_y
  i = 0
  max_item_len = 0

## GET MAX ITEM LENGTH
  for item in list:
    if len(item) > max_item_len:

  if add_max_item_len_to_gap_y:
    gap_y += max_item_len
      max_item_len = len(item)

## ADD STRINGS TO WIN/PAD
  for item in list:
    item_str = str(item)
    win.addstr(x,y,item_str)
    
## INCREASE X and Y COORDINATES
    x += gap_x
    y += gap_y
    
def draw_df(win,df,start_x,start_y,gap_x=0,gap_y=0,add_max_item_len_to_gap_y=False):
  pos = 0
  x = startx
  y = start_y
  i = 0
  max_item_len = 0

## GET MAX ITEM LENGTH
  for item in list:
    if len(item) > max_item_len:

  if add_max_item_len_to_gap_y:
    gap_y += max_item_len
      max_item_len = len(item)

## ADD STRINGS TO WIN/PAD
  for item in list:
    item_str = str(item)
    win.addstr(x,y,item_str)
    
## INCREASE X and Y COORDINATES
    x += gap_x
    y += gap_y

#for index, row in df.iterrows():
#  print(f"Row index: {index}")
#  for column, value in row.iteritems():
#    print(f"Column: {column}, Value: {value}")


def draw_menu(stdscr):
  height, width = stdscr.getmaxyx()

  # DECLARE STRINGS
  title = "Weather Forecast"[:width-1]
  statusbarstr = "Press 'q' to exit | press 'd' for days | press 'w' for weeks"

  # FIND CENTRE FOR TITLE POSITION
  start_x_title = int((width // 2) - (len(title) // 2) - len(title) % 2)
  start_y = int((height // 2) - 2)

  # RENDER STATUS BAR
  stdscr.addstr(height-1, 0, statusbarstr)
  stdscr.addstr(height-1, len(statusbarstr), " " * (width - len(statusbarstr) - 1))

  # BOLD TITLE
  stdscr.attron(curses.A_BOLD)
  stdscr.addstr(start_y, start_x_title, title)
  stdscr.attroff(curses.A_BOLD)
  
  change_menu(stdscr)

def change_menu(stdscr):
  key = stdscr.getch()
  if key == ord('q'):
    quitter()
  if key == ord('d'):
    draw_days(stdscr,'')
  if key == ord('w'):
    draw_week(stdscr)

def draw_days(stdscr,data):
  day_count = 4
  cols_per_day = 6
  max_row_head = 10
  height, width = stdscr.getmaxyx()
  max_days = ( width - 2 - max_row_head - 1) // cols_per_day 

# DEFINE PAD FOR DATA
  pad = curses.newpad(height-2,width-2)

  row_heads = ['Wind Speed','Temp','Rain','Feels']
  draw_list(pad,row_heads,1,1,1,0)
#  pad.addstr(0,0,str(max_days))
  stdscr.refresh()
  pad.refresh(0,0,0,0,height-2,width-2)

  key = stdscr.getch()
  if key == curses.KEY_RIGHT:
    print('placeholder')
### END


def draw_week(stdscr):
  return True

def main(stdscr):
  stdscr.clear()
  draw_menu(stdscr)

if __name__ == "__main__":
  curses.wrapper(main)
