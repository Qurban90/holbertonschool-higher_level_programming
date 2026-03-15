#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
The script takes 3 arguments: mysql username, mysql password, and database name.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Get arguments from command line
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute queries
    cursor = db.cursor()

    # Execute the SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the results
    query_rows = cursor.fetchall()

    # Display the results
    for row in query_rows:
        print(row)

    # Clean up: close cursor and database connection
    cursor.close()
    db.close()
