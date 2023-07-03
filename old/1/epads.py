#!/bin/python3
import curses

# Initialize curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Get screen dimensions
height, width = stdscr.getmaxyx()

# Create two horizontal pads
pad1 = curses.newpad(height//3, width)
pad2 = curses.newpad(height//3, width)
pad1.addstr(1,1,"ABCasdjkfljasddkl;fjasdklfjasdkl;fjkl;asdfjklas;djgasdfjfklasd;jfkl;asda")

# Draw boxes around the pads
pad1.box()
pad2.box()

# Create menu bar
menu = curses.newwin(1, width, height-1, 0)
menu.addstr(0, 0, "Press '1' to focus on Pad 1, '2' to focus on Pad 2")

# Refresh the screen
stdscr.refresh()

# Set initial focus on Pad 1
focus = pad1

# Main loop
while True:
    # Draw the pads and menu
    pad1.refresh(0, 0, 0, 0, height//3-1, width-1)
    pad2.refresh(0, 0, height//3, 0, height//3*2-1, width-1)
    menu.refresh()

    # Get user input
    key = stdscr.getch()

    # Handle user input
    if key == ord('1'):
        focus = pad1
    elif key == ord('2'):
        focus = pad2
    elif key == curses.KEY_LEFT:
        focus.move(0, -1)
    elif key == curses.KEY_RIGHT:
        focus.move(0, 1)
    elif key == curses.KEY_UP:
        focus.move(-1, 0)
    elif key == curses.KEY_DOWN:
        focus.move(1, 0)
    elif key == ord('q'):
        break

# Clean up curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
