#Simple Calculator

x = int(input("Enter first number- "))
y = int(input("Enter second number- "))
z = input("Enter operator(+,-,*,/,%,**) :- ")

if (z=="+"):
    print("Sum is = ",x+y)
elif (z=="-"):
    print("Difference is = ",x-y)
elif (z=="*"):
    print("Product is = ",x*y)
elif (z=="/"):
    print("Division is = ",x/y)
elif (z=="%"):
    print("Module is = ",x%y)
else :
    print("Power is = ",x**y)

