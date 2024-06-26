import psycopg2
import json


def fetch(key):
    try:
        with open('../config.properties', 'r') as file:
            for line in file:
                key_value = line.strip().split('=')
                if len(key_value) == 2:
                    k, v = key_value
                    if k.strip() == key:
                        return v.strip()
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def linear_search(requisite, code):
    for req in requisite:
        if code == req["courseCode"]:
            return req

    return {
        "courseCode": code,
        "req": "Not applicable."
    }


def get_session_number(s):
    s = s.lower()
    if 'first' in s and 'second' in s:
        return "3"
    elif 'second' in s:
        return "2"
    elif 'first' in s:
        return "1"
    else:
        return "NULL"


def get_course_query(c, r):
    if not c["CourseCode"] == r["courseCode"]:
        print("Warning! There exists a mismatch between courses.json and requisites.json. Consider re-running the "
              "scraper and wrangler.")
        print(c["CourseCode"] + " is matched with " + r["courseCode"])
        r = linear_search(open('requisites.json'), c["CourseCode"])

    return (f"INSERT INTO courses(course_code, name, session, career, units, mod, requisite) "
            f"VALUES ('{c['CourseCode']}', '{c['Name']}', {get_session_number(c['Session'])}, '{c['Career']}', {c['Units']}, '{c['ModeOfDelivery']}', '{r['req']}')")


def get_program_query(p):
    fStr = lambda str: 'NULL' if str is None else f"'{str}'"
    fInt = lambda int: 'NULL' if int is None else f"{int}"
    return (f"INSERT INTO programs(program_code, name, atar, career, duration, mod) "
            f"VALUES ({fStr(p['program_code'])}, {fStr(p['name'])}, {fInt(p['atar'])}, {fStr(p['career'])}, {fInt(p['duration'])}, {fStr(p['mod'])})")

def start():
    print('Connecting to postgreSQL database...')
    conn = psycopg2.connect(
        host=fetch("db_host"),
        database=fetch("db_database"),
        port=fetch("db_port"),
        user=fetch("db_username"),
        password=fetch("db_password")
    )
    cursor = conn.cursor()

    courses = json.load(open("courses.json"))
    requisites = json.load(open("requisites.json"))
    programs = json.load(open("programs.json"))

    try:
        print('Deleting existing courses')
        cursor.execute('DELETE FROM courses')
        cursor.execute('DELETE FROM programs')
        print("Updating courses")
        for i in range(len(courses)):
            cursor.execute(get_course_query(courses[i], requisites[i]))
        print("Updating programs")
        for i in range(len(programs)):
            cursor.execute(get_program_query(programs[i]))
        print("Updated courses")
        conn.commit()
    except Exception as e:
        print("Error: unable to fetch data")
        print(e)
    finally:
        print("Done.")
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()


start()
