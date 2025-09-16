#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      acer
#
# Created:     26-08-2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# if else statements:

#age = int(input("Enter age : "))

#if (age >= 18) : print("Adult"), print("You can vote")
#elif(age < 18 and age>3) : print("You are in school"), print("you cannot vote")
#else : print("you are a child")

# Let's build a calculator .

#num1 = int(input("Enter first number : "))
#op = input("Enter operator(+,-,*,/,%,**) : ")
#num2 = int(input("Enter second number : "))

#if (op == "+") : print("Result : ",num1 + num2)
#elif(op == "-") : print("Result : ",num1 - num2)
#elif(op == "*") : print("Result : ",num1 * num2)
#elif(op == "/") : print("Result : ",num1 / num2)
#elif(op == "%") : print("Result : ",num1 % num2)
#elif(op == "**") : print("Result : ",num1 ** num2)
#else : print("Invalid operation")

# Range : range is just the set of numbers.
#num = range(9) # here range(9) = 0, 1,2,3,,4,5,6,7,8. {i.e, all the numbers
#                till 8 but not 9.
#print(num)



# LOOPS

# 1. While loop

a = 1
while(a<= 10) :
   print(a)
   a = a + 1
   if(a==7):
    break

#i = 1
#while(i <10) :
#   print(i * "hello ") #here , * works same as concatenation. The no. of times
#                             you muliply a char ,it will return that character
#                             that no. of times.
#   i = i + 1

#Reversing the pattern
#i= 5
#while(i >= 0):
#    print(i * "*")
#    i = i - 1


# 2. for loop

#for item in range(8) :
#        print(item + 1)

#