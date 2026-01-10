import os, sys, sqlite3

if os.path.exists("twk.db"):
    print("DB exisitiert bereits.")
    sys.exit(0)

connection = sqlite3.connect("twk.db")
cursor = connection.cursor()
sql = "CREATE TABLE personen(" \
        "id INTEGER PRIMARY KEY, " \
        "name TEXT, " \
        "vorname TEXT, " \
        "jahrgang INTEGER, " \
        "klbuchstabe TEXT, " \
        "p1 REAL, " \
        "p2 REAL, " \
        "p3 REAL)"

cursor.execute(sql)

print ("DB created!")