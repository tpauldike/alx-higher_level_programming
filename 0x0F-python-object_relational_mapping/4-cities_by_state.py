#!/usr/bin/python3
"""
A script that lists all cities from the database
'hbtn_0e_0_usa'
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connect to the database and execute the querry that
    will fetch all data from the 'cities' table
    """
    conn = db.connect(host="localhost", port=3306,
                      user=argv[1], passwd=argv[2], db=argv[3])

    with conn.cursor() as cursor:
        cursor.execute("SELECT cities.id, cities.name, states.name \
                                FROM cities JOIN states ON cities.state_id \
                                = states.id ORDER BY cities.id ASC")
    cities = cursor.fetchall()

    if cities is not None:
        for row in cities:
            print(row)
