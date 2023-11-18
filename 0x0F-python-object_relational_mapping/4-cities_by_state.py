#!/usr/bin/python3
'''a script that lists all cities from the database hbtn_0e_4_usa'''
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

    query = "SELECT cities.id, cities.name, states.name \
        FROM cities, states\
        WHERE cities.state_id = states.id \
            ORDER BY cities.id"
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
