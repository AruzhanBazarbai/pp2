import psycopg2

#передаем параметры
conn= psycopg2.connect(
    host='localhost', #укажем где у нас хранится база данных
    database="pp2_test", #укажем саму базу данных
    user="pp2_test", #укажем пользователя
    password="pp2_passsword" #укажем пароль
)

sql='select * from table_name where column_name=row'

cursor=conn.cursor() #с помощью cursor можем выполнять определенные команды
cursor.execute(sql)

print(cursor.fetchone()) #выведет самую первую
print(cursor.fetchmany(size=5)) # выведет только 4
print(cursor.fetchall()) #выведет все

# for row in  cursor:
    # print(row)

cursor.close()
conn.close()