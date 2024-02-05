import timeit

''' Time the function calls, ironically speeds up DB access '''
def time_stuff(some_function):
  def wrapper(*args, **kwargs):
    t0 = timeit.default_timer()
    value = some_function(*args, **kwargs)
    return value
  return wrapper
