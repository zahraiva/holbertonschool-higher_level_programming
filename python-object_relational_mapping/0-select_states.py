#!/usr/bin/python3
"""
Module for Selecting states from the hbtn_0e_0_usa database
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = db.cursor()

    try:
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    
    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        cursor.close()
        db.close()
