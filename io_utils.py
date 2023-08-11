import pickle
import os

def write_pickle(obj, filename=None):
  if not filename:
    try:
      obj_name = obj.__name__
    except AttributeError:
      raise ValueError("No filename provided to write pickle file and object has no __name__ attribute.")
  
    filename = f"data/{obj_name}_{type(obj).__name__}.pickle"

  filename = f"data/{filename}_{type(obj).__name__}.pickle"
  
  with open(filename, "wb") as file:
    pickle.dump(obj, file)
  
  return filename


def load_pickle(filename):
  with open(filename, 'rb') as file:
    obj = pickle.load(file)
  
  return obj


"""
Here's an example usage:

import mypickle

# Example object
my_object = {'name': 'John', 'age': 30}

# Write object to pickle file
pickle_file = mypickle.write_pickle(my_object)

# Load object from pickle file
loaded_object = mypickle.load_pickle(pickle_file)

# Print loaded object
print(loaded_object)
"""
