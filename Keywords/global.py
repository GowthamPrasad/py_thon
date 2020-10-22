#global is used to declare the variable in the global scope
def hw():
  global a
  a = "Hello World"
  b = "Hello Python"

hw()
print(a)
print(b) #it throws an exception NameError as it is defined only inside hw()