#!/usr/bin/python3
"""
A script that lists all the names in the mysql_pld table,
in the attendance database
"""

import MySQLdb

if __name__ == '__main__':
    """
    connect to the database and execute the querry that
    will fetch all data from the 'mysql_pld' table
    """
    conn = MySQLdb.connect(
        host="localhost", user=root, port=3306, passwd=root, db=attendance)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM mysql_pld")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
