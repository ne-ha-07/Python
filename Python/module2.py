#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      acer
#
# Created:     12-09-2023
# Copyright:   (c) acer 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

'''dic = {"Pragya" : 21,
 "Neha": 21,
 "Anjali" : 20,
 "Mona" : 15}
print(dic)
#print(dic["Mona"])
#print(dic.keys())
#print(dic.values())'''

'''a = int(input("Value of a: "))
b = int(input("Value of b: "))
c = int(input("Value of c: "))
d = int(input("Value of d: "))
e = int(input("Value of e: "))

if (a>b, a>c, a>d, a>e) :
    print("a is the largest")

elif (b>a, b>c, b>d, b>e) :
    print("a is the largest")

elif (c>a, c>b, c>d, c>e) :
    print("a is the largest")

elif (d>a, d>b, d>c, d>e) :
    print("a is the largest")

else:
    print("e is the largest")'''


'''# String Slicing

word = "Good Morning"
print(word[0])
print(word[0 : 1])
print(word[0 : 5])
print(word[: 3])
print(word[-3 :])
print(word[3:])
print(word[: -3])'''

'''# Split Strings

str = "Iyi gecelar"
print(str.split(" "))'''

'''str = "Iyi gecelar"
print(str.startswith("I"))
print(str.startswith("i"))
print(str.endswith("r"))
print(str.endswith("a"))
print(str.endswith("lar"))
print(str.replace("Iyi", "Good"))'''

'''# Q. Best of two test average marks out of three test marks accepted by the user.

a = float(input("1st marks : "))
b = float(input("2nd marks : "))
c = float(input("3rd marks : "))

ab = (a + b)/2.0
bc = (b + c)/2.0
ca = (a + c)/2.0

print("Best of two test average marks: ")
if(ab>bc and ab>ca):
    print(ab)
elif(bc>ab and bc>ca):
    print(bc)
else:
    print(ca)'''

'''# Break & Continue Statement.

num = 5
while num<10 :
    #print("Current number : ", num)
    num = num + 1
    if num == 8:
        continue
    print("Current num : ", num)
'''

'''#Features of python :

1. Easy syntax
2. Portablilty
3. Object Oriented
4. Open Source
5. Huge libraries
5. Interpretation - which means written line by line and easy debugging.

'''

'''# Comments- written just to increase the readability of the program.

"#" it tells the code that everythiing after that will be omitted till the line ends.

There are two types of comments :
    a) single line - #hii
    b) multi-line - #hello
                    #how are you?

Q. What are docstrings?

Docstrings are denoted as (3 single quotes), but this is not a comment.
Docstrings are documentation strings written within quotes that acts as a comment.
They are not assigned to any variable, but used as a comment.
They are not omitted by the interpreter, but comments are omitted by the interpreter.'''


'''# Collections.
1. namedtuple

from collections import namedtuple

a = namedtuple('Student', 'Name, Branch, Age')
x = a('Neha', 'cse', '23')
print(x)'''

'''#2. deque

from collections import deque

a = ['a','b', 'c', 'd', 'e', 'f']
n = deque(a)

#operations performed on a deque.
print(n)
n.append('python')   #add an element in the right end by default
print(n)
n.appendleft('java')
print(n)
n.pop()  #delete an element from right end by default
print(n)
n.popleft() #delete from left end
print(n) '''

