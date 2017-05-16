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
        pass


def mentor_names():
    indicator = """SELECT first_name, last_name FROM mentors;"""
    rows = database(indicator)

    for item in rows:
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

    for item in rows:
        print(item[0], end=' ')
        print(item[1], end=' ')
        print(item[2])


def the_lost_hat():
    indicator = """SELECT first_name, last_name, phone_number FROM
                applicants WHERE email LIKE '%adipiscingenimmi.edu%';"""
    rows = database(indicator)

    for item in rows:
        print(item[0], end=' ')
        print(item[1], end=' ')
        print(item[2])


def new_applicant():
    check = """SELECT * FROM applicants WHERE application_code=54823;"""
    check_row = database(check)

    if len(check_row) < 1:
        indicator = """INSERT INTO applicants (first_name, last_name, phone_number, email, application_code)
                    VALUES ('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823');"""
        rows = database(indicator)

    get_row = """SELECT first_name, last_name, phone_number, email, application_code FROM applicants
                  WHERE application_code='54823';"""
    rows = database(get_row)

    for item in rows:
        print(item[0], end=' ')
        print(item[1], end=' ')
        print(item[2], end=' ')
        print(item[3], end=' ')
        print(item[4])


def change_phone_number():
    indicator = """UPDATE applicants SET phone_number = '003670/223-7459'
                WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""
    database(indicator)

    get_indicator = """SELECT first_name, last_name, phone_number FROM applicants
                    WHERE first_name = 'Jemima' AND last_name = 'Foreman';"""

    rows = database(get_indicator)

    for item in rows:
        print(item[0], end=' ')
        print(item[1], end=' ')
        print(item[2])


def delete_applicants():
    indicator = """DELETE FROM applicants WHERE email LIKE '%mauriseu.net%';"""
    rows = database(indicator)
    print("The applicants are removed from the database.")