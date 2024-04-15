#!/usr/bin/python3
# Displays all cities of a given state from the
# states table of the database hbtn_0e_4_usa.
# Safe from SQL injections.
# Usage: ./5-filter_cities.py <mysql username> \
#                             <mysql password> \
#                             <database name> \
#                             <state name searched>
#!/usr/bin/python3
""" This script return cities and states """
if __name__ == '__main__':
    import MySQLdb
    from sys import argv
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities c
                LEFT JOIN states s ON c.state_id = s.id
                WHERE s.name LIKE BINARY %s
                ORDER BY c.id ASC""", (argv[4],))
    rows = cur.fetchall()
    cont = 0
    lista = []
    for row in rows:
        lista.append(row[0])
    print(", ".join(lista))
    cur.close()
    db.close()
