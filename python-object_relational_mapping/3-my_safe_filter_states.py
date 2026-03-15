#!/usr/bin/python3
"""Lists all values in states safely from SQL injection"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    # Parametrləşdirilmiş sorğu: %s istifadə olunur
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    # Arqument ikinci parametr kimi ötürülür ki, MySQLdb onu 'escape' etsin
    cursor.execute(query, (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
