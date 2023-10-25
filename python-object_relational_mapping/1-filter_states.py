#!/usr/bin/python3
"""
Lists states with a name starting with 'N' from the hbtn_0e_0_usa database.
"""

import MySQLdb
import sys


def list_states(username, password, database):
    """
    Lists states with a name starting with 'N' from the specified database.
    """
    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,\
        passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve states starting with 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch all rows and return them
    results = cursor.fetchall()

    # Disconnect from the server
    db.close()

    return results


if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Get and print states using the function
    states = list_states(username, password, database)
    for state in states:
        print(state)