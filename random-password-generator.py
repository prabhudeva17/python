#!/usr/bin/python
import string
import random
char = string.ascii_letters+string.punctuation+string.digits
password = ''.join(random.choice(char) for i in range(20))
print password
