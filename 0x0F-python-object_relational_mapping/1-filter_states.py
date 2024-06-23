#!/usr/bin/python3
"""
A script that list all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            charset="utf8"
            )
    except MySQLdb.Error as e:
        print("Error connecting to database: {}".format(e))
        sys.exit(1)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE \
                    BINARY 'N%' ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
