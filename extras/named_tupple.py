from collections import namedtuple

''' The function to get a cursor description for a resource '''
def namedtuple_factory(cursor, row):
  fields = [column[0] for column in cursor.description]
  cls = namedtuple("Row", fields)
  return cls._make(row)