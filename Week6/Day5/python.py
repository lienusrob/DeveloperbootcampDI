import psycopg2

    conn = psycopg2.connect("dbname='dvdrental' user='lienusrob'    host='localhost' password='[7099Casi]'")

    cur = conn.cursor()
    cur.execute("""SELECT VERSION()""")
    row = cur.fetchone()
    print("Server version is ",row)

except:
    print('You have not connected')