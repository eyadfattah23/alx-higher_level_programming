#!/usr/bin/python3
'''script that lists all states start with N from the database hbtn_0e_0_usa'''
if __name__ == '__main__':
    import MySQLdb
    import sys
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states WHERE name LIKE BINARY %s order by id', ('N%', ))

    records = cursor.fetchall()
    for record in records:
        print(record)