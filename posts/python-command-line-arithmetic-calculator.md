In this mini-tutorial, we will implement a simple arithmetic `calculator` which will get its two `operands` and the `operator`, either from `keyboard input` or from the `command line arguments`.

<!--more-->

The `operators` supported are:

*   addition: `+`
*   subtraction: `-`
*   multiplication: `x`
*   division: `/`

## Get operands and operator:

### From Keyboard input:

We will be using the `raw_input` to read a `string` from keyboard. The two `operands` need to be casted as `float` using `float()` function:

    operand1 = float(raw_input('Enter the first operand: '))    
    operator = raw_input('Enter the operator: ')
    operand2 = float(raw_input('Enter the second operand: '))
    

### From Command line arguments:

-- We will need the `sys` module to get command line arguments:

    import sys
    

-- The shell arguments are retrieved in a list of strings with `sys.argv`. When calling this script, three arguments should be given: `operand1`, `operator`, `operand2`. If the number of arguments provided is less that three, we exit the script with an error message:

    if len(sys.argv) < 4:
        print 'Incorrect number of arguments: Expecting 3 arguments, %d given.' % (len(sys.argv) - 1
        exit()
    

-- If at least three arguments has been given, we get the `operator` and the two `operands` that we convert from `string` to `float`. Note that the first item of `sys.argv` (`sys.argv[0]`) is the `name of the script` executed:

    else:
        operand1 = float(sys.argv[1])
        operator = sys.argv[2]
        operand2 = float(sys.argv[3])
    

-- **This is valid for the previous two types of input:** The casting of the two `operators` from `string` to `float` has to be put inside a `try ... except` block, because the `float()` function will throw a `ValueError` if the argument provided to it could not be parsed as a number.

    else:
        # operands have to be numbers
        try:
            operand1 = float(string_operand1)
            operand2 = float(string_operand2)
        except ValueError, e:
            print e
            exit()
    

## Compute the result:

-- After that, we can compute the result of the operation. The operation change according to the `operand` given:

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == 'x':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2   
    

-- Finally, we print the `result` of the operation with two decimal digits (`.2f`):

    print '%.2f %s %.2f = %.2f' % (operand1, operator, operand2, result)
    

*   The full source code for shell arguments calculator: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-command-line-arithmetic-calculator.py" target="_blank">Python Command Line Arithmetic Calculator on Github</a>

*   The full source code for keyboard input calculator: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-command-line-arithmetic-calculator2.py" target="_blank">Python Command Line Arithmetic Calculator 2 on Github</a>
