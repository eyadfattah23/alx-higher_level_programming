#!/usr/bin/python3
'''a script that lists all cities from the database hbtn_0e_4_usa
takes in the name of a state as an argument and lists
all cities of that state
INJECTION PROPETECTED'''
if __name__ == '__main__':
    import MySQLdb
    import sys
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4].replace('"', '').strip(';')
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)

    cursor = db.cursor()
    cursor.execute('SELECT cities.name \
        FROM cities, states\
            WHERE cities.state_id = states.id \
                AND states.name LIKE BINARY %s\
                ORDER BY cities.id ASC;', (state_name, ))

    records = cursor.fetchall()
    city_names = [record[0] for record in records]

    # Join the city names with commas and print
    cities_str = ", ".join(city_names)
    print(cities_str)
