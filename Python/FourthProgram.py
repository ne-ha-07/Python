#-------------------------------------------------------------------------------
# Name:        module4
# Purpose:
#
# Author:      acer
#
# Created:     24-08-2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

OPERATORS

'''Types of Operators:
   1. Arithmetic operators: +, -, *, /, %(modulo), **(power)
   2. Assignment operators: =, +=, -=, *=, /=, %=, **=
   3. Comparison/ Relational operators: >,<, ==(true/false), !=(not equal to),>=, <=
   4. Logical operators   : and, or, not
   5. Bitwise opeartors   : &(Bitwise AND),|(Bitwise OR), ~(Bitwise NOT),
                         ^(Bitwise XOR), >>(Bitwise right shift), <<(Bitwise
                         left shift)
   6. Special opeartors   : a) Identify operators: is, is not
                               eg : t = input("please enter a character : ")
                                    print("The ASCII value of: " + t + "is" ,ord(t))
#                            b) Membership operators: in, not in
#                               eg : string = "Thank you so much."
#                                    print("so" in string)


#1. Arithmetic operators
#print(5+2)
#print(5-2)
#print(5*2)
#print(5/2)
#print(5%2)
#print(5**2)

#2. Assignment operators
#i = 6
#i += 2
#i -= 2
#i *= 2
#i /= 2
#i %= 2
#i **= 2
#print(i)

#result = 45+6-3*2
#print(result)

#3. Comparison/ Relational  operators

#print(3>2)
#print(3<2)
#print(3==2)
#print(3==3)
#print(3!=2)
#print(3!=3)
#print(3>=2)
#print(3<=2)

#4. Logical operators

# a). or : Two conditions will be there.
#          If both the options are true, it will return true.
#          eg : print(3>2 or 2>1)

#          If both the conditions are false, it will return false.
#          eg : print(3>4 or 2>5)

#          If a single condition is true, it will also return true.
#          eg : print(3>6 or 2>1)

#b). and : only if both the conditions are true, will return true.

#print(2>1 and 1==1)
#print(2!=3 and 9>11)
#print(2==3 and 4!=4)

#c). NOT : it reverse the condition
# eg :print(not 2>3)

# 5. Bitwise operators

#a = 10
#b = 4
#print(a & b)
#print(a | b)
#print( ~b)
#print(a ^ b)
#print(a>> 1)
#print(a<< 2)
