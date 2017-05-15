import psycopg2
import queries


def database():
    try:
        connect_str = "dbname='kristof' user='kristof' host='localhost' password='951125'"
        conn = psycopg2.connect(connect_str)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute("""SELECT first_name, last_name FROM mentors;""")
        rows = cursor.fetchall()
        return rows

    except Exception as e:
        print("Uh oh, can't connect. Invalid dbname, user or password?")
        print(e)


def mentor_names():
    rows = database()
    for index, item in enumerate(rows):
        print(item[1], end=' ')
        print(item[0])


def main():
    mentor_names()

if __name__ == '__main__':
    main()