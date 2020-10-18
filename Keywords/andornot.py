#Logical and, or, not
#and - both the condition should be true
exp=10
age=45
if(exp>=10 and age>=45):
    print("Eligible to work")
else:
    print("Not Eligible")

#or - any one condition should be true
x=10
print(x>5 or x<5)

#not - returns false if the value is true and vice versa
x="True"
print(not(x))