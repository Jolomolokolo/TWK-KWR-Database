import os, sys, sqlite3

searching_id = 0

def db_set_points(searching_id):

    # Punkte erhalten aus Eingabe...
    p1 = 3.5
    p2 = 4.7
    p3 = 10


    if os.path.exists("twk.db"):
        print("Inserting...")
        connection = sqlite3.connect("twk.db")
        cursor = connection.cursor()

        sql = "SELECT * FROM personen WHERE id = ?"
        cursor.execute(sql, (searching_id,))
        
        result = cursor.fetchone()
        print(result)

        sql = "UPDATE personen SET p1 = ?, p2 = ?, p3 = ? WHERE id = ?"
        cursor.execute(sql, (p1, p2, p3, searching_id))
        connection.commit()

        connection.close()
        print("Inserting completed")

    else:
        print("DB not exsists!")
        sys.exit(0)


db_set_points(searching_id)