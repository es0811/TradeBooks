from book import *


#List all books currently listed by the user and the books are available
def list_all_books(conn,email):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book WHERE email=%s and trade_type!=%s',(email,'Sold'))
        books=cursor.fetchall()
        # print(books)
        books_array=[]
        for book in books:
            print(book[0])
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None

# Returns an object of the type book basesd on book number
def get_book(conn,book_number):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book \
        WHERE book_number=%s',(book_number,))
        book=cursor.fetchone()
        return Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0])

    except Exception as e:
        print(e)
        cursor.close()
        return None

#Lists all the books which are currently available for trading. This will show up books only available and listed...
#...by other users
def buy_book_list(conn,email):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book \
        WHERE email!=%s and trade_type!=%s',(email,'Sold',))
        books=cursor.fetchall()
        books_array=[]
        for book in books:
            print(book[0])
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None

#Displays books currently sold for the user who's email is email
def buy_book_list_bytitle(conn,email,title):
    cursor=conn.cursor()
    try:
        param = f"%{title.lower()}%"
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book \
        WHERE email!=%s and trade_type!=%s and LOWER(title) LIKE %s',(email,'Sold',param,))
        books=cursor.fetchall()
        books_array=[]

        for book in books:
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None

#Lists all books available for trading when searched by genre
def buy_book_list_bygenre(conn,email,genre):
    cursor=conn.cursor()
    try:
        cursor.execute('SELECT book_number, title,author,genre, description,pages,condition,cover, email,trade_type,cost FROM book \
        WHERE email!=%s and trade_type!=%s and genre=%s',(email,'Sold',genre,))
        books=cursor.fetchall()
        books_array=[]
        for book in books:
            books_array.append(Book(book[1],book[2],book[3],book[4],book[5],book[6],book[7],book[8],book[10],book[9],book[0]))
        cursor.close()
        return books_array
    except Exception as e:
        print(e)
        cursor.close()
        return None

#This task is executed when the buy book button is pressed.
def buy_book(conn,book,email):
    cursor=conn.cursor()
    try:
        cursor.execute('UPDATE book SET trade_type=%s WHERE book_number=%s',('Sold',book.book_number,))
        conn.commit()
        cursor.execute('INSERT INTO alltrades(book_number,email,trade_date) VALUES(%s,%s,now())',(book.book_number,email,))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        cursor.close()
        return None
