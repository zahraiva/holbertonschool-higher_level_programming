#!/usr/bin/python3
"""
Module for Selecting genres and counting linked shows
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()

    try:
        cursor.execute("""SELECT * FROM states ORDER BY id""")
        rows = cursor.fetchall()
    except MySQLdb.Error as e:
        print(e)

    for row in rows:
        print(row)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()
