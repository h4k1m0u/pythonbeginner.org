#!/usr/bin/env python
import string
import random

# password length and characters set
LENGTH = 10
letters = string.letters
digits = string.digits
charset = letters + digits

# generate a 10 characters pseudo-random alphanumeric password
password_list = [random.choice(charset) for i in xrange(LENGTH)]
password = ''.join(password_list)
print password
