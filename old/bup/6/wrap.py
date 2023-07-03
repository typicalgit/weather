#!/usr/bin/env python3
import sys

try:
    # Get the name of the local .py file from the command line argument
    filename = sys.argv[1]

    # Execute the local .py file within a try block
    try:
        exec(open(filename).read())
    except Exception as e:
        # Customize the traceback message with the line number of the error
        tb = sys.exc_info()[2]
        line = tb.tb_lineno
        print(f"Error on line {line}: {e}")

except IndexError:
   print("Please provide the name of the local .py file as an argument.")
