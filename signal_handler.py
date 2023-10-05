import signal
import sys
import os

def delete_files():
  directory = os.path.join(os.getcwd(), "data")
  for filename in os.listdir(directory):
    if filename.endswith(".pickle"): 
      file_path = os.path.join(directory, filename)
      os.remove(file_path)

def sigint_handler(signal, frame):
  print("SIGINT received. Exiting...")
  quitter()

def setup_signal_handlers():
  signal.signal(signal.SIGINT, sigint_handler)
  # Add more signal handlers here if needed

def quitter():
  delete_files()
  sys.exit(0)
  

