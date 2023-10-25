#!/usr/bin/python3
# List all states from a given db sorted in ascending order by id
# Username, password, and database names are given as user args
import MySQLdb
import sys


if __name__ == "__main__":
    # Get MySQL credentials from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to retrieve id and name columns from the states table and sort by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all rows and display them as in the example
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()
