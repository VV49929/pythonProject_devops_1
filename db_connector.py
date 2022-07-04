import pymysql


# Establishing a connection to DB
from pymysql import IntegrityError



# Getting a cursor from Database

#### create connection
def create_connection_to_DB():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='rQd80nAEyy', passwd='dPyiHYZpL8', db='rQd80nAEyy')
    return conn
####  close conn
def close_conn(conn):
    conn.close()

# Getting all data from table “users”
def get_user_by_id(user_id):
    conn = create_connection_to_DB()
    cursor = conn.cursor()
    tuple1 = (user_id)
    cursor.execute("SELECT name FROM rQd80nAEyy.users where id=%s",tuple1)
    if cursor.rowcount == 0:
        user_name =  ""
    for row in cursor:
        user_name = row[0]
    cursor.close()
    close_conn(conn)
    return user_name

def delete_user_by_id(user_id):
    conn = create_connection_to_DB()
    cursor = conn.cursor()
    conn.autocommit(True)
    tuple1 = (user_id)
    cursor.execute("DELETE FROM rQd80nAEyy.users where id=%s",tuple1)
    if cursor.rowcount == 0:
        rc = -1
    else:
        rc = 0
    cursor.close()
    close_conn(conn)
    return rc



def add_user_to_table(user_name, user_id):
    '''
    Add user to users table.

            Parameters:
                    user_name (string): name of user
                    user_id (int): ID numner of the user

            Returns:
                    -1 if not success
                    0  if insert success
    '''

    conn = create_connection_to_DB()
    cursor = conn.cursor()
    tuple1 = (user_name,user_id)
    try:
       conn.autocommit(True)
       cursor.execute("INSERT into rQd80nAEyy.users (name, id) VALUES (%s,%s)",tuple1)
    except IntegrityError:
       cursor.close()
       conn.close()
       return -1
    return 0

def update_user_name(user_name, user_id):
    conn = create_connection_to_DB()
    cursor = conn.cursor()
    conn.autocommit(True)
    tuple1 = (user_name, user_id)
    cursor.execute("update rQd80nAEyy.users set name = %s where id = %s",tuple1)
    if cursor.rowcount == 0:
       rc = -1
    else:
       rc = 0
    cursor.close()
    conn.close()
    return rc


def get_all_users():
    conn = create_connection_to_DB()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM rQd80nAEyy.users;")
    print(cursor.rowcount)
    # Iterating table and printing all users
    for row in cursor:
        print(row)
    cursor.close()
    conn.close()

def get_first_free_id():
    '''
    Returns the first free ID in users table.

            Returns:
                    free_number (): free ID number in user table
    '''

    conn = create_connection_to_DB()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM rQd80nAEyy.users order by id;")
    print(cursor.rowcount)
    counter=0
    # Iterating table and printing all users
    for row in cursor:
        counter += 1
        if row[0] > counter:
          break
    cursor.close()
    conn.close()
    return counter


# aa = get_user_by_id(50)
# print("{"+aa+"}")

rc = add_user_to_table('israel11',3)
print("insert: " + str(rc))
#
rc = update_user_name('israel1',11)
print("update: " + str(rc))


rc = delete_user_by_id(11)
print("delete: " + str(rc))


get_all_users()
print(get_first_free_id())
print(get_first_free_id.__doc__)
print(add_user_to_table.__doc__)