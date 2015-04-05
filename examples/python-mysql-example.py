#!/usr/bin/env python
import MySQLdb

db = MySQLdb.connect(host='localhost', user='root', passwd='root', db='python')

# app loop
while True:
    # read user input
    c = raw_input('\nEnter your command [L]ist, [A]dd, [Q]uit: ')

    if (c == 'l'):
        # get all persons from database
        cur = db.cursor()
        cur.execute('SELECT * FROM persons')
        for row in cur.fetchall():
            print row
        cur.close()
    elif (c == 'a'):
        # add a person to database
        name = raw_input('Enter person name to insert: ')
        cur = db.cursor()
        cur.execute('INSERT INTO persons(name) VALUES (%s)', (name,))
        cur.close()
    elif (c == 'q'):
        # quit application
        break

# close connection
db.close()
