from os.path import exists, relpath

def get_db_name():
  db_name = ''
  path = relpath("data_base/db_names.txt")

  if exists(path) is not False:
    with open(path, 'r') as f:
      fn = f.read()
      db_name = fn.split(' ').pop(0).lower()
  
  return db_name