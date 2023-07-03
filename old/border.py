#!/bin/python3
import curses

def draw_border(window):
  window.box()
  # Get the dimensions of the window
  height, width = window.getmaxyx()

  # Draw the top and bottom borders
  window.hline(0, 0, curses.ACS_HLINE, width)
  window.hline(height-1, 0, curses.ACS_HLINE, width)

  # Draw the left and right borders
  window.vline(1, 0, curses.ACS_VLINE, height - 2)
  window.vline(1, width-1, curses.ACS_VLINE, height - 2)

  # Draw the corners
#  window.addch(0, 0, curses.ACS_ULCORNER, curses.color_pair(1))
#  window.addch(0, width-1, curses.ACS_URCORNER, curses.color_pair(1))
#  window.addch(height-1, 0, curses.ACS_LLCORNER, curses.color_pair(1))
#  window.addch(height-1, width-1, curses.ACS_LRCORNER, curses.color_pair(1))

  # Draw the inner border
##  window.border(curses.ACS_VLINE, curses.ACS_VLINE, curses.ACS_HLINE, curses.ACS_HLINE,curses.ACS_ULCORNER, curses.ACS_URCORNER, curses.ACS_LLCORNER, curses.ACS_LRCORNER) #,curses.color_pair(1))
#
  window.refresh()

def bla(stdscr):
  k = 0
  win = stdscr.subwin(6,6,1,1)
  win.addstr(1,1,"A")
  draw_border(win)
  win.refresh()
  while k != ord('q'):
    stdscr.refresh()
    k = stdscr.getch()

def main():
  curses.wrapper(bla)


main()



