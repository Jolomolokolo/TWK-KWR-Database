import os, sys, sqlite3, csv
from db_create import dbCreate

csv_files = "Klasse-8A.csv"

if os.path.exists("twk.db"):
    print("Importing...")
    connection = sqlite3.connect("twk.db")
    cursor = connection.cursor()

    cursor.execute("SELECT MAX(id) FROM personen")
    result = cursor.fetchone()
    next_id = (result[0] + 1) if result[0] is not None else 0

    with open(csv_files) as csvdatei:
        csv_reader_object = csv.reader(csvdatei, delimiter=',')
        
        next(csv_reader_object)
        
        # Check if Person mit gleichem Namen, Vornamen und Geburtstag schon exsistiert...

        for row in csv_reader_object:
            if len(row) >= 5:
                name = row[0]
                vorname = row[1]
                jahrgang = int(row[2])
                klbuchstabe = row[3]
                geburtstag = row[4]
                p = None

                sql = "INSERT INTO personen VALUES(?,?,?,?,?,?,?,?,?)"
                cursor.execute(sql, (name, vorname, next_id, jahrgang, klbuchstabe, geburtstag, p, p, p))
                
                print(f"Imported: {vorname} {name} (ID: {next_id})")
                next_id = next_id + 1
        
        connection.commit()

    print("Importing succesful")
else:

    # Funktion für automatisches erstellen, also Abbruch vermeiden

    dbCreate()
    sys.exit(0)
