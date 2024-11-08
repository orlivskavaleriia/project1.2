import time
import psycopg2
from psycopg2 import OperationalError

def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user="postgres",
                password="postgresd",
                host="backend_rds", 
                port="5432"
            )
            conn.close()
            break
        except OperationalError:
            print("Waiting for PostgreSQL...")
            time.sleep(5)

if __name__ == "__main__":
    wait_for_postgres()
