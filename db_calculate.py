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
            age = None

        connection.close()
        
        if total != None and age != None:
            certificate = calculate_certificate(age, total)
            print(certificate)
        
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

def calculate_certificate(age, total_points):
    if not isinstance(total_points, float) or total_points < 0:
        certificate = "Certificate impossible!"
        print("Certificate is impossible - total points is impossible")
        sys.exit(0)

    match age:
        case _ if age < 10:
            if total_points <= 8:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 10:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 10:
            if total_points <= 10:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 12:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 11:
            if total_points <= 12:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 14:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 12:
            if total_points <= 14:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 16:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 13:
            if total_points <= 16:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 18:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 14:
            if total_points <= 18:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 20:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 15:
            if total_points <= 20:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 22:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 16:
            if total_points <= 22:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 24:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case 17:
            if total_points <= 24:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 26:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"
        case _ if age >= 18:
            if total_points <= 26:
                certificate = "Teilnehmerurkunde"
            elif total_points <= 28:
                certificate = "Siegerurkunde"
            elif total_points < 30:
                certificate = "Ehrenurkunde"

        case _:
            print("Not valid age")

    return certificate


db_calculate_full_points(searching_id)