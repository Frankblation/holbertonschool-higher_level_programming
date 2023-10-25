#!/usr/bin/python3
"""Displays name argument of states table"""
import MySQLdb
import sys


def filters_names_safe():
    """
    Only lists with states that matches name argument
    """
    if len(sys.argv) == 5:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])

        cur = db.cursor()

        cur.execute("SELECT * FROM states WHERE BINARY name='{:s}'\
                    ORDER BY id ASC".format(sys.argv[4]))
        rows = cur.fetchall()
        for id in rows:
            print(id)

        cur.close()
        db.close()
    else:
        return

if __name__ == "__main__":
    filters_names_safe()