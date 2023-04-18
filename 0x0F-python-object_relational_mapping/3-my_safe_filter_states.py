#!/usr/bin/python3
"""
A script (safe from MySQL injections)
that displays all values in the states
table of the database `hbtn_0e_0_usa`,
where `name` matches the argument passed
to it at run time
"""

import MySQLdb as db
from sys import argv

if __name__ == '__main__':
    """
    connect to the database and fetch all data
    from the 'states' table
    """
    conn = db.connect(host="localhost", port=3306,
                      user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE \
                    BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    rows = cursor.fetchall()

    for row in rows:
        print(row)
