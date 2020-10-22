#raise is used to throw an exception by the user
a=int(input("Enter a number:"))
b=1/a
if b==0:
    raise Exception("Zero Division Error")
else:
    print(b)