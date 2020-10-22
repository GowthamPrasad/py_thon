#Nonlocal is similar to global, is used to declare that a variable inside a nested function
def hw():
  global a
  a = "Hello World"
  b = "Hello Python"
  def display():
    nonlocal b
  print(a)
  print(b)

hw()