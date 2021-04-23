# part 1
import psycopg2
from config import config

def connect():
    #Connect to the postgresql database server
    conn=None
    try:
        #read connection parameters
        params=config()

        #connect to the postgresql server
        conn = psycopg2.connect(**params)

        #create a cursor
        cur=conn.cursor()

        cur.execute('SELECT version()')

        db_version=cur.fetchone()
        print(db_version)
        cur.close()
    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()

connect()
