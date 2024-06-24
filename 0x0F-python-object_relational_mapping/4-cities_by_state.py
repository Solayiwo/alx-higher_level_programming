#!/usr/bin/python3
"""
A script that lists all cities from the database hbtn_0e_4_usa
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
    cursor.execute("SELECT cities.id, cities.name, states.name FROM \
                    cities JOIN states ON cities.state_id \
                    = states.id ORDER BY cities.id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
