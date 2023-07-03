#!/bin/python3
import curses

def main(stdscr):
    # Clear the screen
    stdscr.clear()
    stdscr.refresh()

    # Create a new pad with enough space to display the alphabet
    pad = curses.newpad(6, 126)
    pad.box()

    # Write the alphabet to the pad
    for i in range(26):
        pad.addstr(0, i, chr(ord("a") + i))

    # Refresh the pad to display its contents
    pad.refresh(0, 0, 0, 0, curses.LINES - 1, curses.COLS - 1)
    stdscr.refresh()

    # Wait for the user to press 'q'
    while True:
        ch = stdscr.getch()
        if ch == ord('q'):
            break

if __name__ == '__main__':
    curses.wrapper(main)
