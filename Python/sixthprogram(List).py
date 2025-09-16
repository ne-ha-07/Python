#-------------------------------------------------------------------------------
# Name:        module6
# Purpose:
#
# Author:      acer
#
# Created:     29-08-2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''List : A complex datatype, wihich has collection of primitive datatypes.

marks = [98, 94, 93, 90,] # here, the variable named 'marks' is a list.
print(marks[2])   #[2] is the index number of the list we want to print.

print(marks[-1])   #[-1] means that we want to print the last number.

print(marks[0 : 2])   # [0 : 2] means we want only first 2 numbers(1st and 2nd)
                    NOTE : the list having index number 2 won't be printing.

print(marks[1 : 4])

 Applying loops in list.
 1. For loop:
for score in marks :
    print(score)

 Many operations also can be done in list.
( .append, .insert, index , len, clear, .extend, count(), index() )



 To add marks in the given list , we use append operator.
eg :
marks = [98, 94, 93, 90,]
marks.append(100)
print(marks)

 To add a number in between the list and not in the end, we use insert.
eg :
marks = [98, 94, 93, 90,]
marks.insert(2, 100) # first write the index then the value you want to print.
print(marks)

marks = [98, 94, 93, 90,]
marks.insert(2, 100)
to check whether any number exists in the list or not.
print(100 in marks)

 To know the length of the list.
marks = [98, 94, 93, 90,]
marks.insert(2, 100)
print(len(marks))


 2. While loop.

marks = [70, 75, 80, 85, 90]

i = 0
while i < len(marks) :
    print(marks)
    i = i + 1

marks.clear()    #To add a blank list.
print(marks)'''

# python program to print the element in the list which is divisible by 5.

#a = [1, 2, 5, 3, 10, 8, 15, 20, 12, 25, 50]
#for i in a:
#    if i%5==0:
#           print(i)
#           break
#else:
#        print("not found")


a = int(input("Enter a number: "))

print("Cube of", a ,"is",a**3,".")