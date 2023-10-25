#!/usr/bin/python3
# List all states from a given db sorted in ascending order by id
# Username, password, and database names are given as user args
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    cursor = db.cursor()


    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    host = 'localhost'
    port = 3306
    list_states(username, password, database_name, host, port)
