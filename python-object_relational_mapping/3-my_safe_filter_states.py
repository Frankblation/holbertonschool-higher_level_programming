#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches
the argument (safe from MySQL injection).
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    search_term = sys.argv[4]
./h

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    search_term_with_percent = f"%{search_term}%"

    cursor.execute(query, (search_term_with_percent,))
    results = cursor.fetchall()

    for row in results:
        print(row)

    db.close()
