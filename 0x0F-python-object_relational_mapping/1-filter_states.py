#!/usr/bin/python3
"""
List all states, that has the letter `N`
as the first letter of its name, from the
database `hbtn_0e_0_usa`
"""

import MySQLdb as db
from sys import argv

"""
connect to the database and fetch all data
from the 'states' table
"""

if __name__ == '__main__':
    conn = db.connect(host="localhost", port=3306,
                      user=argv[1], passwd=argv[2], db=argv[3])
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")

    rows_fetched = cursor.fetchall()

    for row in rows_fetched:
        print(row)
