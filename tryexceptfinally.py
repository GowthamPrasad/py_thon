#try is used to test a block of code
try:
    x=open("hw.txt","r")
#if exception occurs, except block is executed
except:
    print("File not found...Must've deleted or moved")
#no matter what the outcome of try...except, finally will be executed
finally:
    print("Task Complete")