#lambda is used to create an anonymous function (function with no name)
# It is an inline function that does not contain a return statement
a = lambda x: x*2
for i in range(1,6):
    print(a(i))