#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa that starts with N'''
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name)

    cur = conn.cursor()

    states = cur.execute(
        "SELECT * FROM states where name like BINARY %s order by id", ('N%', ))

    rows = cur.fetchall()
    for row in rows:
        print(row)
