#!/bin/python3
import time 
import curses

def draw_daily_win(stdscr):
  height, width = stdscr.getmaxyx()
  height2, width2 = stdscr.getyx()
  pad_height = height // 2 - 2
  pad_width = width + 100
  daily_pad = curses.newpad(pad_height,pad_width)
  daily_pad.addstr(4,2,str(width))
  daily_pad.addstr(5,2,str(width2))
#TL
  daily_pad.addstr(2,2,"tltltl")
#BL
  daily_pad.addstr(pad_height - 3,2,"blblbl")
#TR
  daily_pad.addstr(2,pad_width - 5,"trtr")
#BR
  daily_pad.addstr(pad_height - 3,pad_width - 5,"brbrbr")
  daily_pad.box()
  daily_pad.refresh(0,0,0,0,height - 2,width - 2)
  daily_pad.scrollok(True)
#  daily_pad.scroll(100)
#  daily_pad.refresh(0,width,0,0,height - 2,width - 2)

def main(stdscr):
  stdscr.clear()
  stdscr.refresh()
  draw_daily_win(stdscr)
  key = 0
  while key != ord('q'):
    key = stdscr.getch()

# initialize curses
curses.wrapper(main)
