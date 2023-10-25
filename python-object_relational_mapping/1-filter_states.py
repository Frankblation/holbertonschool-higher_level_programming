#!/usr/bin/python3
"""
Lists states with a name starting with 'N' from the hbtn_0e_0_usa database.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials and search term from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_term = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Use format to create the SQL query with user input
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format
    (search_term)

    # Execute SQL query
    cursor.execute(query)

    # Fetch all rows and display them as in the example
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Disconnect from the server
    db.close()
