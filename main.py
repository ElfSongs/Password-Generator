#Password generator
import string
import random
number = int(input("How many letters should your password contain?"))
#number = random.randint(8,11)
abc = string.ascii_lowercase
abc_list = list(abc)
password = []
while number > 0:
    x = random.choice(abc_list)
    random_caps = random.randint(0,1)
    if random_caps == 0:
        x = str.capitalize(x)
    password.append(x)
    number = number -1
password = ''.join(password)
print(password)
