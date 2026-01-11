import os, sys, sqlite3
from datetime import datetime, date

searching_id = 0
def db_calculate_full_points(searching_id):

    if os.path.exists("twk.db"):
        print("Calculations...")
        connection = sqlite3.connect("twk.db")
        cursor = connection.cursor()

        sql = "SELECT p1, p2, p3 FROM personen WHERE id = ?"
        cursor.execute(sql, (searching_id,))

        result = cursor.fetchone()
        if result:
            p1, p2, p3 = result
            if all(v is None for v in (p1, p2, p3)):
                total = None
            else:
                total = (p1 or 0) + (p2 or 0) + (p3 or 0)
            print(f"p1: {p1}, p2: {p2}, p3: {p3}")
            print(f"Total points: {total}")
        else:
            print("No person with this ID")

        sql = "SELECT geburtstag FROM personen WHERE id = ?"
        cursor.execute(sql, (searching_id,))

        result = cursor.fetchone()
        if result:
            geburtstag = result[0]
            print(f"Birthday: {geburtstag}")
            age = calculate_age(geburtstag)
            print(f"Age: {age} Years")
        else:
            print("No Birthday found")

        connection.close()
        print("Calculations completed")

    else:
        print("DB not exsists!")
        sys.exit(0)

def calculate_age(born):
    born = datetime.strptime(born, "%d.%m.%Y").date()
    today = date.today()
    try: 
        birthday = born.replace(year=today.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year



db_calculate_full_points(searching_id)