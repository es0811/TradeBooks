class Reader:
    def __init__(self,email,username,password,fname,lname,add1,add2,postalcode,books_sold,books_rented,books_rented_out,books_purchased):
        self.email=email
        self.username=username
        self.password=password
        self.fname=fname
        self.lname=lname
        self.add1=add1
        self.add2=add2
        self.postalcode=postalcode
        self.books_sold=books_sold
        self.books_rented=books_rented
        self.books_rented_out=books_rented_out
        self.books_purchased=books_purchased

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def get_id(self):
        return str(self.email)

#This method returns the object user for the email id
    @staticmethod
    def get(conn,email):
        cursor=conn.cursor()
        cursor.execute('SELECT email,username,fname,lname,address_line1,address_line2,postal_code,books_sold,books_rented,books_rented_out,books_purchased FROM reader WHERE email=%s',(email,))
        user=cursor.fetchone()
        reader=None
        if user:
            reader=Reader(user[0],user[1],None,user[2],user[3],user[4],user[5],user[6],user[7],user[8],user[9],user[10])
        return reader

#This function verifies if the username and the password are correct.
    @staticmethod
    def validate_credentials(conn,email,password):
        cursor=conn.cursor()
        cursor.execute('SELECT CASE WHEN EXISTS ( \
        SELECT * \
        FROM reader\
        WHERE email = %s)\
        THEN CAST(1 AS BIT)\
        ELSE CAST(0 AS BIT) END',(email,))
        email_exists=cursor.fetchone()[0]
        if email_exists=='0':
            return None,'Email does not exist!'
        cursor.execute('SELECT password FROM reader WHERE email=%s',(email,))
        stored_password=cursor.fetchone()[0]
        print(stored_password,password)
        if(stored_password!=password):
            return None, 'Invalid password!'
        cursor.execute('SELECT email,username,fname,lname,address_line1,address_line2,postal_code,books_sold,books_rented,books_rented_out,books_purchased FROM reader WHERE email=%s',(email,))
        user=cursor.fetchone()
        reader=Reader(user[0],user[1],None,user[2],user[3],user[4],user[5],user[6],user[7],user[8],user[9],user[10])
        return reader,''
