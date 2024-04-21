import psycopg2


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


conn = psycopg2.connect(
    host=fetch("db_host"),
    database=fetch("db_database"),
    port=fetch("db_port"),
    user=fetch("db_username"),
    password=fetch("db_password")
)
