#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      acer
#
# Created:     24-08-2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# STRINGS

string = "You are brave enough."

#print(string.upper())
#-> It will change all the characters inside the string into uppercase.

#print(string.lower())
#-> It will change all the characters inside the string into lowercase.

#print(string)
#-> It will print the same string as above again.

#print(string.find("g"))
#pov: Y is at the zeroth position.
#-> It is to find the index number of the charcter.
#-> output= It will tell the index number of that character.
#If any number is not found in the string, it will return the number -1.
#eg: print(string.find(x))
#output : -1

#We can also find the index number of a substring.
#eg: print(string.find("brave"))

#We can also replace a character from our string.
#print(string.replace("brave", "strong"))

#Also can identify whether the character exists in the string or not, by using
# 'in'.
#print("You" in string)
#It will return True.