#!/bin/python3
import curses

def main(stdscr):
    key = 0
    # Clear the screen
    stdscr.clear()

    # Get the screen dimensions
    height, width = stdscr.getmaxyx()

    # Create the two pads
    pad1 = curses.newpad(height // 3, width)
    pad2 = curses.newpad(height // 3, width)

    # Draw a box around the first pad
    pad1.box()

    # Draw some text in the first pad
    pad1.addstr(1, 1, "This is pad 1" + str(width))

    # Draw a box around the second pad
    pad2.box()

    # Draw some text in the second pad
    pad2.addstr(1, 1, "This is pad 2")

    # Create the menu bar
    menu_bar = curses.newwin(1, width, height - (height // 3), 0)

    # Draw the menu bar
    menu_bar.addstr(0, 0, "Press 1 to switch to pad 1, 2 to switch to pad 2")

    # Refresh the screen
    stdscr.refresh()
    menu_bar.refresh()

    # Set the initial active pad to pad 1
    active_pad = pad1

    # Loop forever
    while key != ord('q'):
        # Get the user's input
        key = stdscr.getch()

        # If the user pressed 1, switch to pad 1
        if key == ord('1'):
            active_pad = pad1
            menu_bar.clear()
            menu_bar.addstr(0, 0, "Press h to move left, l to move right in pad 1")
            active_pad.box()
        # If the user pressed 2, switch to pad 2
        elif key == ord('2'):
            active_pad = pad2
            menu_bar.clear()
            menu_bar.addstr(0, 0, "Press h to move left, l to move right in pad 2")
            active_pad.box()
        # If the user pressed h, move left in the active pad
        elif key == ord('h'):
            active_pad.scroll(0, -1)
        # If the user pressed l, move right in the active pad
        elif key == ord('l'):
#            active_pad.move(0,1)
            active_pad.scroll(0,1)

        # Refresh the screen
        stdscr.refresh()
        menu_bar.refresh()
        active_pad.refresh(0,0,0,0,height,width)
# Start the app
curses.wrapper(main)

