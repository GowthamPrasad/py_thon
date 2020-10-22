#yield is used inside a function like a return statement, returns a generator
def generator():
    for i in range(6):
        yield i*i

a = generator()
for i in a:
    print(i)