We are going to need two built-in python modules; i.e. `sys` and `time`:

    import sys import time
    

First, we create an infinite loop:

    while True:
    

Then, we use the `carriage return` (`\r`), to make the cursor return to the first character of the same line before every print (notice the `,` at the end of the `print` statement that makes the `print` stay on the same line):

    print '\r' + 'time in HH:MM:SS format',
    

`strftime` without a second parameter will print the current time according to the string formatting given as a first argument (`Hours:Minutes:Seconds`):

    print '\r' + time.strftime("%H:%M:%S"),
    

The following instruction forces the text to print to be sent to the console `stdout`:

    sys.stdout.flush()
    

Finally, we make the script `sleep` for one second to wait for system clock to update:

    time.sleep(1)
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-command-line-clock.py" target="_blank">Python Command Line Clock on Github</a>
