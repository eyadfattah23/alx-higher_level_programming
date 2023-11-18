#!/usr/bin/python3
'''a script that lists all states from the database hbtn_0e_0_usa
where name matches the argument.'''
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    mysql_username = argv[1]
    mysql_password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_password,
                           db=database_name)

    cur = conn.cursor()

    query = "SELECT * FROM states WHERE name like \
        binary %s ORDER BY id"
    states = cur.execute(
        query, (state_name_searched, ))

    rows = cur.fetchall()
    for row in rows:
        print(row)
