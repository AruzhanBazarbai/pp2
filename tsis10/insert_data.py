# part 3
import psycopg2
from config import config

#inserting one row

def insert_vender(vendor_name):
    sql='''INSERT INTO vendors(vendor_name)
           VALUES(%s)
           RETURNING vendor_id;
        '''
    conn=None
    vendor_id=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.execute(sql,(vendor_name,))
        vendor_id=cur.fetchone()[0]
        conn.commit()
        cur.close()
    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()

    return vendor_id

#Inserting multiple rows

def insert_vendor_list(vendor_list):
    sql='''INSERT INTO vendors(vendor_name)
           VALUES(%s)
        '''
    conn=None
    try:
        params=config()
        conn=psycopg2.connect(**params)
        cur=conn.cursor()
        cur.executemany(sql,vendor_list)
        conn.commit()
        cur.close()
    except Exception as e:
        print(e)

    if conn is not None:
        conn.close()

print(insert_vender('Aruzhan'))
insert_vendor_list([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
