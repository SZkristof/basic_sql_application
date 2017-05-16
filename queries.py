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
    indicator = """SELECT first_name, last_name FROM mentors;"""
    rows = database(indicator)

    for index, item in enumerate(rows):
        print(item[1], end=' ')
        print(item[0])


def mentor_nicks():
    indicator = """SELECT nick_name FROM mentors WHERE city='Miskolc';"""
    rows = database(indicator)

    for item in rows:
        print(item[0])


def finding_carol():
    indicator = """SELECT first_name, last_name, phone_number FROM applicants WHERE first_name='Carol';"""
    rows = database(indicator)

    for index, item in enumerate(rows):
        print(item[0], end=' ')
        print(item[1], end=' ')
        print(item[2])


def the_lost_hat():
    indicator = """SELECT first_name, last_name, phone_number FROM applicants WHERE email LIKE '%adipiscingenimmi.edu%';"""
    rows = database(indicator)

    for index, item in enumerate(rows):
        print(item[0], end=' ')
        print(item[1], end=' ')
        print(item[2])
