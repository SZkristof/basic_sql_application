import psycopg2


def database(indicator):
    try:
        connect_str = "dbname='kristof' user='kristof' host='localhost' password='951125'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(indicator)
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def mentor_names():
    rows = database(indicator="""SELECT first_name, last_name FROM mentors;""")
    for index, item in enumerate(rows):
        print(item[1], end=' ')
        print(item[0])


def mentor_nicks():
    rows = database(indicator="""SELECT nick_name FROM mentors WHERE city='Miskolc';""")
    for item in rows:
        print(item[0])
