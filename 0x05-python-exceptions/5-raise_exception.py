def raise_exception():
    raise TypeError
try:
  raise_exception()
except TypeError:
  print("TypeError raised")
