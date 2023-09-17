#!/usr/bin/python3
'''script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa
where name matches the argument.'''
if __name__ == '__main__':
    import MySQLdb
    import sys
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4].strip("'")
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM states \
            WHERE name = "{}" COLLATE utf8mb4_unicode_ci order by id'.format(state_name))
    records = cursor.fetchall()
    for record in records:
        print(record)
