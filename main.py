from secrets import PASSWORD
import psycopg2

conn = psycopg2.connect(host="localhost", dbname="twkdb", user="postgres", password=PASSWORD, port="5432")


cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS person (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender CHAR
);
""")


conn.commit()

cur.close()
conn.close()