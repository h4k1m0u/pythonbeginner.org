-- To install the `Python`'s `MySQL` driver (`MySQLdb`) on `Freebsd`:

    pkg install py27-MySQLdb-1.2.3_4
    

<!--more-->

-- Create a database named `python` and add a `persons` table to it. Use the `mysql` shell command for that:

    mysql -h localhost -u <user> -p<password>
    CREATE DATABASE python;
    USE python;
    CREATE TABLE persons(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100)
    );
    

-- We start the `python` script by importing the `mysql` driver that we have just installed:

    import MySQLdb
    

-- After that, you connect to the created `python` database, using the same `mysql` credentials used earlier on the command line:

    db = MySQLdb.connect(host='localhost', user='<user>', passwd='<password>', db='python')
    

-- Next, we will add an infinite loop (app loop), inside of which we will read a `character` from `keyboard`:

    while True:
        c = raw_input('Enter your command [L]ist, [A]dd, [Q]uit: ')
    

The character entered can have the following values:

*   **l**: List the `persons` inside the `persons` table.
*   **a**: Add a `person` to the `persons` table.
*   **q**: Quit the application (the main loop).

## Listing persons:

In this case, we create a `cursor` object that we are going to use to retrieve all `persons` from the database using a very basic `MySQL` query: `SELECT * FROM persons`. Then, we loop over the list of tuples returned by `cur.fetchall()` and we print each tuple `row`. Don't forget to close the cursor, as we usually use a unique `cursor` for each `query`.

    if (c == 'l'):
        cur = db.cursor()
        cur.execute('SELECT * FROM persons')
        for row in cur.fetchall():
            print row
        cur.close()
    

## Inserting a new person:

We read the `name` string that we will insert into the `name` column of the `persons` database table, from `keyboard`. Same as for the `SELECT` query, we create a `cursor` object that we close at the end of the `insertion` block. The `INSERT` is very simple too `INSERT INTO persons(name) VALUES (%s)`, just notice that the `name` string is passed as a tuple in the second argument and not as a `string substitution` directly in the query to the `execute()` method, to avoid a `SQL Injection`.

    elif (c == 'a'):
        name = raw_input('Enter person name to insert: ')
        cur = db.cursor()
        cur.execute('INSERT INTO persons(name) VALUES (%s)', (name,))
        cur.close()
    

## Exiting the application:

Lastly, if the user enter `q` we exit the infinite loop:

    elif c == 'q':
        break
    

-- At the end of the script, we close the connection to the `MySQL` database:

    db.close()
    

The full source code: <a href="https://github.com/h4k1m0u/pythonbeginner.org/blob/master/examples/python-mysql-example.py" target="_blank">Python MySQL Example on Github</a>
