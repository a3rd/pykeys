import curses

def main(stdscr):
    # do not wait for input when calling getch
    stdscr.nodelay(1)
    while True:
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # print numeric value
            stdscr.addstr(str(c) + ' ')
            #stdscr.addstr(c)
            stdscr.refresh()
            # return curser to start position
            stdscr.move(0, 0)

        if c == 49:
            print "1"

        if c == 50:
            print "2"
        
        if c == 51:
            print "3"

        

if __name__ == '__main__':
    curses.wrapper(main)
