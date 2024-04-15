#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.
# Usage: ./2-my_filter_states.py <mysql username> \
#                                <mysql password> \
#                                <database name> \
#                                <state name searched>
#!/usr/bin/python3
""" This script return filter states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY id""".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
