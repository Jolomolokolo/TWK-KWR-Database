import os, sys, sqlite3

def dbCreate():

    if os.path.exists("twk.db"):
        print("DB exsits already")
        sys.exit(0)

    connection = sqlite3.connect("twk.db")
    cursor = connection.cursor()
    sql = "CREATE TABLE personen(" \
            "name TEXT, " \
            "vorname TEXT, " \
            "id INTEGER PRIMARY KEY, " \
            "jahrgang INTEGER, " \
            "klbuchstabe TEXT, " \
            "geburtstag TEXT, " \
            "p1 REAL, " \
            "p2 REAL, " \
            "p3 REAL)"

    cursor.execute(sql)

    print ("DB created")