#!/usr/bin/env python
import sys
import time

while True:
    print '\r' + time.strftime("%H:%M:%S"),
    sys.stdout.flush()
    time.sleep(1)
