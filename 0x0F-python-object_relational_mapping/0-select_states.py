#!/usr/bin/python3
"""
A script that lists all states from the database
'hbtn_0e_0_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connect to the database and execute the querry that
    will fetch all data from the 'states' table
    """
    conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
