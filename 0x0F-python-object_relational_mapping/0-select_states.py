#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa'''
if __name__ == '__main__':
    import MySQLdb
    import sys
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    cursor = db.cursor()
    cursor.execute('SELECT * FROM states order by id')

    records = cursor.fetchall()
    for record in records:
        print(record)
