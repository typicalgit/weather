#!/usr/bin/env python3

def write_to_file(object,out_file):
  with open(out_file,'w') as file:
    file.write(object)
  file.close()

