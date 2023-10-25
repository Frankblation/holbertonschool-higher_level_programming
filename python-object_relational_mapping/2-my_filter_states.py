#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches
the argument.
"""

import MySQLdb
import sys


def display_states(username, password, database_name, state_name):
    """
    Displays states from the hbtn_0e_0_usa database where
     name matches the provided argument.
    """
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".\
        format(state_name)

    cursor.execute(query)

    results = cursor.fetchall()

    for state in results:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    display_states(username, password, database_name, state_name)
