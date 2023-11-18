#!/usr/bin/python3
'''a script that lists all cities from the database hbtn_0e_4_usa
that belong to the state_name_searched given as an argument'''
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

    query = "SELECT cities.name \
        FROM cities \
        INNER JOIN states \
        ON cities.state_id = states.id \
            WHERE states.name LIKE BINARY %s\
            ORDER BY cities.id"

    cur.execute(query, (state_name_searched, ))

    rows = cur.fetchall()

    for row in range(len(rows)):
        for col in rows[row]:
            if row + 1 != len(rows):
                print("{}, ".format(col), end='')
            else:
                print("{}".format(col), end='')
    print()
