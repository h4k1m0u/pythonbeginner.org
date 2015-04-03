#!/usr/bin/env python

# get operands & operator from keyboard
try:
    operand1 = float(raw_input('Enter the first operand: '))
except ValueError, e:
    print e
    exit()

operator = raw_input('Enter the operator: ')

try:
    operand2 = float(raw_input('Enter the second operand: '))
except ValueError, e:
    print e
    exit()

# calculate the result according to the operator
if operator == '+':
    result = operand1 + operand2
elif operator == '-':
    result = operand1 - operand2
elif operator == 'x':
    result = operand1 * operand2
elif operator == '/':
    result = operand1 / operand2

# show result
print '%.2f %s %.2f = %.2f' % (operand1, operator, operand2, result)
