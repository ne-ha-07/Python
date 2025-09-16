#-------------------------------------------------------------------------------
# Name:        module5
# Purpose:
#
# Author:      acer
#
# Created:     25-08-2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Q1. Familiarisation with the programming environment Coding Block.
#     Write a pyhton program to print bio-data.

#bio = "Displaying a Bio- Data:"
#print(bio.upper())

#print("Name : Neha Mehto")
#print("Class : CSE- B")
#print("Roll No. - 223121")
#print("Father's Name: Mahesh Kumar")
#print("Mother's Name: Kiran")
#print("Mobile no. - 8810596129")
#print("Email : neha_223121@saitm.org")
#print("Address: D- 54/2, Chattarpur Extn. ND- 118736")

# Q2. Write a program in python to print ASCII values using ord() method.

#K = input("Please enter a Character:")

#print("The ASCII value of" + K + "is" , ord(K))


#Q. Write a python program to swap two numbers.

#Before Swapping
#a = 4
#b = 5

#temp = a
#a = b
#b = temp

#print("The value of a after swapping : {}" .format(a))
#print("The value of b after swapping : {}" .format(b))

# Q, write a python program to convert specified no. of days into years, weeks
#    and days.

#number_of_days = int(input("Enter the Number of days: "))

#calculating years
#Years = (number_of_days) / 365

#calculating weeks
#Weeks = (number_of_days % 365) / 7

#calculating days
#Days = (number_of_days % 365) % 7

#print(Years)
#print(Weeks)
#print(Days)

# Q. Write a program to calculate simple interest.

#P = int(input("Enter principle amount(in Rs.) : "))
#R = int(input("Enter the annual rate(in Rs. ): "))
#T = int(input("Enter the time period(in years) : "))

#Simple_interest =  str(P * R * T / 1000)

#print("S.I. is = " + Simple_interest)


#Q. Write a program to find area of a trianle.

#B = int(input("Base of a Triangle(in cm) : "))
#H = int(input("Height of a Triangle(in cm) : "))

#Area = str(B * H * 1/2)
#print("Area of a triangle is(in cm square) : " + Area)


# Q. convert char from int usinf chr() method.

#number = 100
#result = chr(number)

#print("Integer - {} converted to character - " .format(number), result)


#Q. to find the largest among the three numbers.

#a = int(input("Enter the first number : "))
#b = int(input("Enter the second number : "))
#c = int(input("Enter the third number : "))

#if (a >= b) and (a >= c) : largest = a
#elif (b >= a) and (b >= c) : largest = b
#else : largest = c

#print("The largest number is", largest)


# Q. to find whether the number is odd or even.

#a = int(input("Enter a number : "))

#if (a % 2) == 0 : print("{0} is Even".format(a))

#else : print("{0} is odd".format(a))


# Q. Write a program to perform all arithmetic operations using the if and
#    elif statement.

#a = 5
#b = 4
#c = a + b
#d = a - b
#e = a * b
#f = a / b
#g = a % b
#h = a ** b

# Q. Write a program to convert celsius into fahrenheit.

#C = int(input("Enter the temp. in Celcius : "))
#F = str((9/5 * C) + 32)

#print("The temp. in F is : " + F)

# Q. Write a program to check whether the integers are multiple of 5 or not.

#x = int(input("Enter the integer : "))


#if(x % 5) == 0 : print("{0} is multiple of 5".format(x))
#else : print("{0} is not a multiple of 5".format(x))


# Q. Write a program to print the table of 2 and 13 using for loop.

#num = 2
#for i in range(1, 11) :
#    print(num ,'x', i, '=', num*i)


#num = 13
#for i in range(1, 11) :
#    print(num, 'x', i, '=', num*i)

# Q. Write a program to print factorial of a number.

#num = int(input("Enter a number : "))
#factorial = 1
#if num < 0 :
#    print("Sorry, the factorail of a negative number does not exist")
#elif num == 0 :
#    print("The factorail of 0 is 1")
#else :
#    for i in range(1, num + 1):
#        factorial = factorial*i
#    print("The factorial of" , num,"is = " ,factorial)

# Q. Write a program to print fibonacci series using for loop.

#first = 0
#second = 1

#print(first)
#print(second)

#for x in range(1 , 11) :
#     third first + second
#     first, second = second, third


# Q. Write a program to check if a no. is prime or not.

#num = int(input("Enter a number : "))

#flag = False

#if num == 1 :
#    print(num, "is not a prime number.")
#elif num > 1 :
#    for i in range(2 , num):
#        if (num % i) == 0:
#            flag = True
#            break

#if flag :
#    print(num, "is not a prime number")
#else :
#    print(num, "is a prime number")


# Q. Write a program to display all the multiples of 3 within the range(1 to 50)

#out = print("Output is : ")
#for i in range(3, 50, 3) :
#    print(i)


# Q. Write a program to print the element from 1 to 10 in reverse order using while loop.

#i= 10
#while(i >= 1):
#    print(i)
#    i = i - 1


# Q. Write a program to calculate the length of any string in python.

#str = "Neha"
#print("The length of string is ", len(str))

# Q.

#string = "NETWORK BULLS WHERE CARRERS FLY"
#print(string[ : 13])

#string = "NETWORK BULLS WHERE CARRERS FLY" [ :: -1]
#print(string)

#string = "Kill two birds with a stone"
#print(string.upper())

#string = "Kill two birds with a stone"
#print(string.title())

#string = "Kill two birds with a stone"
#print(string.capitalize())

Bio = "My name is {name}, I’m from {place}.".format(name = "Divyanshu", place = "Uttarakhand")
print(Bio)

