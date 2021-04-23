# psql - клиент который соединяет с базой данных

# \l or \list - list of database

# \c database_name - connect to database (default)

# \dt - list of tables (current database)

# psql -h localhost -U database_name

# psql --help

SELECT:

# 1.select * from table_name; \\ выведет все данные которые есть в этой базе данных
 
# 2.select * from table_name where user_type='STANDARD TABLE; \\* - mean all

# 3. select * from table_name where user_type='BLOGER' AND subscription_id=63; \\OR   

# 4.select id, user_type, subcription_id from name_of_table where user_type='BLOGER' and subscription_id=64;

# 5. select id, user_type, subcription_id from table_name where user_type='BLOGER' limit=10;

#  6. select id, user_type, subcription_id from table_name where user_type='BLOGER' order by subscription_id limit=10; - otsortiruet

#  7. select id, user_type, subcription_id from table_name where user_type='BLOGER' order by subscription_id desc limit=10; - naoborot otsortiruet 

INSTRUCTION-

# install postgres

# pip install psycorg2 (and additional libs)

TO CREATE A USER:

# create user name_of_user with password 'password';

TO CREATE A DATABASE:

# create database name_of_user;

ДАТЬ ПРИВИЛЕГИЮ НА ВСЮ БАЗУ ДЛЯ ДАННОГО ПОЛЬЗОВАТЕЛЯ:

# grant all privileges on database database_name to user_name;

ЧТОБЫ ЗАЙТИ НА ЮЗЕР

# psql -h localhost -U name_of_user

DROP TABLE OR DATABASE:

# drop table table_name;

# drap database database_name;

TO INSERT DATA TO TABLE:

# insert into accounts(column1,column2,...) values(value1,value2,...);
# RETURNING*;

# example:
# insert into accounts(username,password,email,created_on) values('aruzhan','password','aruzhanart@mail.ru','2021-04-22');

TO UPDATE DATA:

#  update table_name set column1='value1'... where user_id=1;

# example:

#  update accounts set username='Aisha' where user_id=2;

TO DELETE DATA:

# delete from table_name where column=value;

# Если вы хотите передать значения оператору DELETE, вы используете 
# заполнители ( %s) в операторе DELETE и передаете входные значения второму параметру метода execute ().

INSTRUCTION ON CREATING TABLE:

        '''
        CREATE TABLE vendors(
            vendor_id SERIAL PRIMARY KEY,
            vendor_name VARCHAR(255) NOT NULL
        )
        ''',
        '''
        CREATE TABLE parts(
            part_id SERIAL PRIMARY KEY,
            part_name VARCHAR(255) NOT NULL
        )
        ''',

        '''
        CREAT TABLE part_drawings(
            part_id INTEGER PRIMARY KEY,
            file_extension VARCHAR(5) NOT NULL,
            drawing data BYTEA NOT NULL,
            FOREIGN KEY (part_id),
            REFERENCES parts(part_id)
            ON UPDATE CASCADE ON DELETE CASCADE

        )
        ''',

    FOREIGN KEY (part_id),
    REFERENCES parts(part_id):

    # В данном случае столбец, указанный после FOREIGN КЕY - это столбец текущей таблицы, 
    # именно ДЛЯ НЕГО будет проверяться ограничение. После REFERENCES указываются данные 
    # родительской таблицы - ее имя и столбцы, ПО НИМ будет проверяться ограничение

ON UPDATE CASCADE ON DELETE CASCADE:

CASCADE-

# -ON DELETE CASCADE означает, что если родительская запись удалена, любые дочерние записи также будут удалены. 

# -ON UPDATE CASCADE означает, что при изменении родительского первичного ключа значение потомка также изменится,
#  чтобы отразить это.

# -ON UPDATE CASCADE ON DELETE CASCADE означает, что если вы UPDATE ИЛИ DELETE родитель, изменения каскадно относятся к ребенку. 
# Это эквивалентно AND результатам первых двух утверждений.
 
SERIAL-

# обычно интеджер и берется последующие числа

HOW CONNECT AND CURSOR WORK:

# If the connection was created successfully, the connect() function returns a new connection object, otherwise, 
# it throws a DatabaseError exception.
# Next, create a new cursor by calling the cursor() method of the connection object. The cursor object is used to execute SELECT statements.

# Если соединение было создано успешно, функция connect() возвращает новый объект соединения, 
# в противном случае она выдает исключение DatabaseError.
# Затем создайте новый курсор, вызвав метод cursor() объекта connection. Объект cursor используется для выполнения операторов SELECT.

INNER JOIN

# Самый простой вид соединения INNER JOIN – внутреннее соединение. 
# Этот вид джойна выведет только те строки, если условие соединения выполняется (является истинным, т.е. TRUE). 
'''
SELECT
#   -- Перечисляем столбцы, которые хотим вывести
  Сотрудники.id,
  Сотрудники.Имя,
  Отделы.Наименование AS Отдел #-- выводим наименование отдела и переименовываем столбец через as
FROM
#   -- таблицы для соединения перечисляем в предложении from 
  Сотрудники
#   -- обратите внимание, что мы не указали вид соединения, поэтому выполнится внутренний (inner) джойн
  JOIN Отделы
    # -- условия соединения прописываются после ON
    # -- условий может быть несколько, записанных через and, or и т.п.
    ON Сотрудники.Отдел = Отделы.