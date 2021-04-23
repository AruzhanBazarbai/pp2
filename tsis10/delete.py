#part 6
import psycopg2 
from config import config

def delete_part(part_id):
    conn=None
    deleted_rows=0
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute('DELETE FROM vendors WHERE vendor_id=%s',(part_id,))
        deleted_rows=cur.rowcount
        conn.commit()
        cur.close()
    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()

    return deleted_rows

print(delete_part(2))