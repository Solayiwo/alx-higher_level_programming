#!/usr/bin/python3
"""
A script that takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    input_arg = sys.argv[4]

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
    cursor.execute("""SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %(state_name)s
            ORDER BY
                cities.id ASC """, {'state_name': input_arg})
    states = cursor.fetchall()

    if states is not None:
        print(", ".join([state[1] for state in states]))

    cursor.close()
    db.close()
