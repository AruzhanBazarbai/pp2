import psycopg2
from config import config

def connect(sql):
    conn=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute(sql)
        row=cur.fetchmany()
        for r in row:
            print(r)
    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()

connect('\dt')