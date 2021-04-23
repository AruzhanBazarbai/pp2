#part 5
import psycopg2
from config import config

#using the method fetchone()
def get_vendors():
    conn=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute('SELECT vendor_name,vendor_id FROM vendors ORDER BY vendor_name')
        print('the number of parts:',cur.rowcount)
        row=cur.fetchone()
        

        while row is not None:
            print(row)
            row=cur.fetchone()

        cur.close()
    except Exception as e:
            print(e)

    if conn is not None:
            conn.close()

#using the method fetchall()

def get_parts():
    conn=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute('SELECT part_name,part_id FROM parts ORDER BY part_name')
        rows=cur.fetchall()
        print('the number of parts:',cur.rowcount)
        
        

        for row in rows:
            print(row)

        cur.close()
    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()


#using the method fetchmany()

def item_row(cursor,size):
    while True:
        rows=cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def get_parts_vendors():
    conn=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute(
            '''
            SELECT part_name,vendor_name
            FROM parts
            INNER JOIN vendor_parts ON vendor_parts.part_id=parts.part_id
            INNER JOIN vendors ON vendors.vendor_id=vendor_parts.part_id
            ORDER BY part_name;
            '''

        )

        for row in item_row(cur,10):
            print(row)
        cur.close()
    except Exception as e:
        print(e)
    
    if conn is not None:
            conn.close()


get_parts_vendors()

get_vendors()
get_parts()













