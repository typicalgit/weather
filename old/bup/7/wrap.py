#!/usr/bin/env python3
import sys
import re

try:
  # Get the name of the local .py file from the command line argument
  filename = sys.argv[1]

  # Execute the local .py file within a try block
  try:
    exec(open(filename,'r').read())
  except Exception as e:

    # FIND ERR LINE NUM IN EXECUTED FILE
    pattern = r"line \d{1,4}"
    match = re.search(pattern, str(e))

    # Customize the traceback message with the line number of the error
    tb = sys.exc_info()[2]
    line = tb.tb_lineno

    # IF ERR LINE NUM FOUND PRINT
    if match:
      print(match.group(0))
    print(f"Error on line {line}: {e}")
    print(str(tb))
    if match:
      print(match.group(0))

except IndexError:
   print("Please provide the name of the local .py file as an argument.")
