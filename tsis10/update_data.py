#part 4
import psycopg2
from config import config

def update_vendor(vendor_name,vendor_id):
    sql='''UPDATE vendors
                SET vendor_name=%s
                WHERE vendor_id=%s
            '''
    conn=None
    updated_rows=0
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute(sql,(vendor_name,vendor_id))
        updated_rows=cur.rowcount
        conn.commit()
        cur.close()

    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()

    return updated_rows

update_vendor('aruzhan',2)