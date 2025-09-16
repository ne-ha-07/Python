#importing the desired modules

import random
import string

#To generate a strong password, characters and digits are used.

x = string.ascii_letters + string.digits + string.punctuation

l = int(input("Input the length of the password: "))

Password = ''.join(random.choices(x, k=l))
print("Your password is:", Password)