import re
#validate the user credentials when the user is registering
def input_validation(conn,email, username):
    print(email)
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if not re.fullmatch(regex,email):
      return False,'Please enter a valid email!'

    cursor=conn.cursor()
    cursor.execute('SELECT CASE WHEN EXISTS ( \
    SELECT * \
    FROM reader\
    WHERE email = %s)\
    THEN CAST(1 AS BIT)\
    ELSE CAST(0 AS BIT) END',(email,))
    email_exists=cursor.fetchall()[0]
    print(email_exists)
    if email_exists=='1':
        return False,'Email already exists!'

    cursor.execute('SELECT CASE WHEN EXISTS ( \
    SELECT * \
    FROM reader\
    WHERE username = %s)\
    THEN CAST(1 AS BIT)\
    ELSE CAST(0 AS BIT) END',(username,))
    username_exists=cursor.fetchall()[0]
    print(username_exists)
    if username_exists=='1':
        return False,'Username already exists!'
    cursor.close()
    return True,''

#Once the validation is performed, the register user function will execute query to insert the user in the database.
def register_user(conn,reader):
    cursor=conn.cursor()
    try:
        print(reader.email, reader.username, reader.password,reader.add1, reader.add2, reader.postalcode)
        cursor.execute('INSERT INTO reader(email, username, password,fname,lname,address_line1, address_line2, postal_code, books_sold, books_rented, books_rented_out, books_purchased) \
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,0,0,0,0)',(reader.email, reader.username, reader.password, reader.fname,reader.lname,reader.add1, reader.add2, reader.postalcode,))
        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return False
