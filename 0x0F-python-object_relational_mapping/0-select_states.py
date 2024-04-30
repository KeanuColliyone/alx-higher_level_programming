#!/usr/bin/python3
"""
A script to list all states from the database `hbtn_0e_0_usa`.
This script takes 3 arguments: mysql username, mysql password, and database name.
Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

def list_states(username, password, dbname):
    """
    Connects to a MySQL database and lists all states in the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
