import curses

def main(stdscr):
### turn off cursor blinking
    curses.curs_set(0)
### get screen dimensions
    sh, sw = stdscr.getmaxyx()
### create two windows
    window1 = curses.newwin(sh-1, sw, 0, 0)
    window2 = curses.newwin(1, sw, sh-1, 0)

    # create menu bar
    menu = ["File", "Edit", "View", "Help"]
    current_menu = 0

    # loop until user exits
    while True:
        # clear windows
        window1.clear()
        window2.clear()

        # draw menu bar
        for i, item in enumerate(menu):
            if i == current_menu:
                window2.addstr(0, i*10, item, curses.A_REVERSE)
            else:
                window2.addstr(0, i*10, item)

        # refresh windows
        window1.refresh()
        window2.refresh()

        # get user input
        key = stdscr.getch()

        # handle user input
        if key == curses.KEY_LEFT:
            current_menu = (current_menu - 1) % len(menu)
        elif key == curses.KEY_RIGHT:
            current_menu = (current_menu + 1) % len(menu)
        elif key == ord("q"):
            break

if __name__ == "__main__":
    curses.wrapper(main)
