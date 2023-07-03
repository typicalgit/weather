#!/bin/python3
import curses

def draw_border(window):
    # Get the dimensions of the window
    height, width = window.getmaxyx()

    # Draw the top and bottom borders
    window.hline(0, 0, curses.ACS_HLINE, width, curses.color_pair(1))
    window.hline(height-1, 0, curses.ACS_HLINE, width, curses.color_pair(1))

    # Draw the left and right borders
    window.vline(0, 0, curses.ACS_VLINE, height, curses.color_pair(1))
    window.vline(0, width-1, curses.ACS_VLINE, height, curses.color_pair(1))

    # Draw the corners
    window.addch(0, 0, curses.ACS_ULCORNER, curses.color_pair(1))
    window.addch(0, width-1, curses.ACS_URCORNER, curses.color_pair(1))
    window.addch(height-1, 0, curses.ACS_LLCORNER, curses.color_pair(1))
    window.addch(height-1, width-1, curses.ACS_LRCORNER, curses.color_pair(1))

    # Draw the inner border
    window.border(curses.ACS_VLINE, curses.ACS_VLINE, curses.ACS_HLINE, curses.ACS_HLINE,
                  curses.ACS_ULCORNER, curses.ACS_URCORNER, curses.ACS_LLCORNER, curses.ACS_LRCORNER,
                  curses.color_pair(1))
def main(stdscr):
  # Clear the screen
  stdscr.clear()

  # Create two full-screen windows
  win1 = curses.newwin(curses.LINES, curses.COLS // 2, 0, 0)
  draw_border(win1)
  win1.border()
  win2 = curses.newwin(curses.LINES, curses.COLS // 2, 0, curses.COLS // 2)

  # Create two horizontal pads in each window
  pad1 = curses.newpad(curses.LINES, curses.COLS // 2)
  pad2 = curses.newpad(curses.LINES, curses.COLS // 2)
  pad1.addstr(0, 0, "This is pad 1")
  pad2.addstr(0, 0, "This is pad 2")

  # Add the pads to the windows
  win1.refresh()
  win2.refresh()
  pad1.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS // 2 - 1)
  pad2.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS // 2 - 1)

  # Create a navigation window at the bottom
  navwin = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)
  navwin.addstr(0, 0, "Press 'q' to quit, '1' to go to window 1, '2' to go to window 2")

  # Loop until the user quits
  while True:
    # Get user input
    c = stdscr.getch()

    # Handle user input
    if c == ord('q'):
      break
    elif c == ord('1'):
      win1.refresh()
      pad1.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS // 2 - 1)
    elif c == ord('2'):
      win2.refresh()
      pad2.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS // 2 - 1)

  # Clean up
  curses.endwin()

if __name__ == '__main__':
  curses.wrapper(main)

