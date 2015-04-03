-- Two built-in python modules are needed to generate an `alphanumeric` password: `string` module and `random` module:

    import string 
    import random
    

<!--more-->

-- We start by defining the password `length` and the password `charset` (The set from which the password is going to pick its characters). We set the `charset` as the concatenation of `alphabetic` (`uppercase` and `lowercase` letters) and `numeric` characters:

    LENGTH = 10
    letters = string.letters
    digits = string.digits
    charset = letters + digits
    

-- Then, we use a <a href="https://docs.python.org/2/tutorial/datastructures.html?highlight=list%20comprehension#list-comprehensions" target="_blank">List Comprehension</a> to build a list of `LENGTH` elements, where each element represent a character which is randomly-picked from the `charset` using <a href="https://docs.python.org/2/library/random.html#random.choice" target="_blank">random.choice()</a>:

    password_list = [random.choice(charset) for i in xrange(LENGTH)]
    

-- Next, we join the password's list into a string using the empty character `''`:

    password = ''.join(password_list)
    

-- Finally, we print the generated `password` to `stdout`:

    print password
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-password-generator.py" target="_blank">Python Password Generator on Github</a>
